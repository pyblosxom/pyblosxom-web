#######################################################################
# This file is part of PyBlosxom.
#
# Copyright (c) 2011 Will Kahn-Greene
#
# PyBlosxom is distributed under the MIT license.  See the file
# LICENSE for distribution details.
#######################################################################

"""
This script generates registry entries for plugins from the plugin
itself.
"""

import os
import ast
import sys


# skip these because they're not plugins
SKIP = ("akismet.py", "__init__.py", "tests")


HELP = """update_registry <plugindir> <outputdir>

Goes through plugins it finds in the plugindir and generates registry
entries for them.  It puts the registry entries in a directory hierarchy
denoted by outputdir.

Docstrings for plugins should be formatted in restructured text.
"""


ENTRYTEMPLATE = """%(title)s
#author %(author)s
#email %(email)s
#infourl %(infourl)s
#download %(download)s
#summary %(summary)s
#license %(license)s
#registrytags %(registrytags)s
#generator update_registry

%(body)s
"""

def get_info(node, info_name):
    # FIXME - this is inefficient since it'll traverse the entire ast
    # but we only really need to look at the top level.
    for mem in ast.walk(node):
        if not isinstance(mem, ast.Assign):
            continue

        for target in mem.targets:
            if not isinstance(target, ast.Name):
                continue

            if target.id == info_name:                
                return mem.value.s

    print "missing %s" % info_name
    return None


def build_registry_entry(filepath):
    try:
        fp = open(filepath, "r")
    except (IOError, OSError):
        return False

    node = ast.parse(fp.read(), filepath, 'exec')

    return ENTRYTEMPLATE % {
        "title": os.path.splitext(os.path.basename(filepath))[0],
        "author": get_info(node, "__author__"),
        "email": get_info(node, "__email__"),
        "infourl": get_info(node, "__url__"),
        # "download": get_info(node, "__download__"),
        "download": "As of PyBlosxom 1.5 rc1, comes with PyBlosxom",
        "summary": get_info(node, "__description__"),
        "license": get_info(node, "__license__"),
        "registrytags": get_info(node, "__registrytags__"),
        "body": ast.get_docstring(node, True)}


def save_entry(filepath, entry):
    parent = os.path.dirname(filepath)
    if not os.path.exists(parent):
        os.makedirs(parent)

    f = open(filepath, "w")
    f.write(entry)
    f.close()


def get_plugins(plugindir, outputdir):
    for root, dirs, files in os.walk(plugindir):
        # remove skipped directories so we don't walk through them
        for mem in SKIP:
            if mem in dirs:
                dirs.remove(mem)
                break

        if root == plugindir:
            continue

        for file_ in files:
            if ((file_.startswith("_") or not file_.endswith(".py") or
                 file_ in SKIP)):
                continue

            filename = os.path.join(root, file_)
            print "working on %s" % filename

            entry = build_registry_entry(filename)

            output_filename = filename[len(plugindir):]
            output_filename = output_filename.lstrip(os.sep)
            output_filename = os.path.splitext(output_filename)[0] + ".rst"
            output_filename = os.path.join(outputdir, output_filename)

            save_entry(output_filename, entry)


def main(args):
    print "update_registry.py"
    print args

    if "-h" in args or "--help" in args:
        print HELP
        return 0

    # this is silly, but it makes the later computation easier
    args.insert(0, "")
    args.insert(0, "")

    outputdir = args.pop()
    if outputdir:
        outputdir = os.path.abspath(outputdir)
    else:
        print "No outputdir specified."
        print HELP
        sys.exit(1)

    plugindir = args.pop()
    if plugindir:
        plugindir = os.path.abspath(plugindir)
    else:
        print "No plugindir specified."
        print HELP
        sys.exit(1)

    print "plugindir: %s" % plugindir
    if not os.path.exists(plugindir):
        print "Plugindir doesn't exist."
        print HELP
        sys.exit(1)

    print "outputdir: %s" % outputdir
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    get_plugins(plugindir, outputdir)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
