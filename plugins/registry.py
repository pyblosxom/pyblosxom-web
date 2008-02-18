"""
This plugin handles displaying a file registry, submitting new entries
to a registry, and comments for existing entries.  A registry 
is a series of .txt files which provide information about a given series 
of things which are registered.  They are organized into categories by 
the directory structure.  

The registry plugin can use entries parsed by other entry parsers so long
as they support meta information.  It supports preformatters and 
postformatters and all that stuff because it uses the regular entry parsers.

The registry requires several templates in your data directory:

  - registry-summary - used for an entry summary line
  - registry-story   - used for a complete single entry
  - registry-index   - used to hold a bunch of summaries

The registry plugin requires a registry-summary template in your data
directory.  This is used to provide a summary of a given registry
entry.

The registry will support the following urls:

    /registry                 -- listing by date (mtime)
    /registry?sortby=category -- listing by category
    /registry?sortby=input    -- listing by any input (author, name, ...)
    /registry/category        -- prints contents in a category
    /registry/path/to/item    -- prints full contents of specific item

The registry plugin requires the following variables to be set in
your config.py file:

    registry_dir    - the directory holding your registry entries
    registry_edit   - whether (1) or not (0) you allow people to submit
                      new entries
    registry_default_flavour - the default flavour to use for the registry
                      if none are requested--defaults to "html"


Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Copyright 2002 - 2008 Will Guaraldi

Revisions:
2.2 - (18 February, 2008) overhauled by removing a bunch of stuff
2.1 - (13 December, 2004) fixed date_head template issue
2.0 - (05 May, 2004) total overhaul--literally
1.4 - (17 March, 2004) bug fixes
1.3 - (17 Feb, 2004) added the ability to see the queue
1.2 - (31 Dec, 2003) complete overhaul for registry submission, updates,
      code refactoring, adjustments for making it easier to adjust, and
      a bunch of other stuff.
1.1 - (3 May, 2003) Minor changes.
1.0 - Created.
"""
import time, re, os.path, os, string
from Pyblosxom.entries import fileentry, base
from Pyblosxom import tools

__author__ = "Will Guaraldi - willg at bluesock dot org"
__version__ = "2.1 (13 December, 2004)"
__url__ = "http://www.bluesock.org/~willg/pyblosxom/"
__description__ = "Handles editing and display of a tree of data files like entries or whatever."

# this is the url that will trigger this plugin into action
TRIGGER = "/registry"

INIT_KEY = "registry_file_initiated"

REGISTRY_SUMMARY = """<li><a href="$base_url/$trigger/$file_path">$name</a>: $briefdesc</li>"""

REGISTRY_STORY = """
<div class="registry_item">
<div class="registry_item_title">$title</div>
<table>
<tr><td class="blosxomRegistryHeader">name:</td><td>$name</td></tr>
<tr><td class="blosxomRegistryHeader">version:</td><td>$version</td></tr>
<tr><td class="blosxomRegistryHeader">author:</td><td>$author</td></tr>
<tr><td class="blosxomRegistryHeader">description:</td><td>$description</td></tr>
<tr><td class="blosxomRegistryHeader">category:</td><td>$category</td></tr>
<tr><td class="blosxomRegistryHeader">url:</td><td>$url</td></tr>
<tr><td class="blosxomRegistryHeader">download:</td><td>$download</td></tr>
<tr><td class="blosxomRegistryHeader">last edited:</td><td>$date</td></tr>
</table>
</div>
"""

CONTRIB_DESC = """
This used to come in the ./contrib directory of the PyBlosxom tar.gz
download.  As of PyBlosxom 1.1, we no longer distribute contributed
plugins with PyBlosxom.  There are various good reasons for this, though
we do apologize for the inconvenience it causes.

Contributed plugins periodically are released as contributed plugin
packs in a big .tar.gz file.  You can get that here:

https://sourceforge.net/project/showfiles.php?group_id=67445&package_id=145140

Between releases, you can get plugins from the SVN repository here:

http://pyblosxom.svn.sourceforge.net/viewvc/pyblosxom/trunk/contrib/plugins/
"""

URLRE = None

def urlme(req, vd, arg1):
    """
    Takes in the request and the argument and converts everything 
    in the argument that resembles a url into an a href.  Then it 
    returns the converted thing.
    """
    global URLRE

    if not URLRE:
        URLRE = re.compile("(http[s]?://[^\\s\\>\\<]+)", re.I)

    sin = arg1
    # FIXME - this could be sped up by using a buffer for "done"
    # pieces.
    mo = URLRE.search(sin)
    while mo:
        s = mo.start()
        e = mo.end()
        if sin[e-1] == "." or sin[e-1] == ",":
            e = e - 1
        newtext = '<a href=\"%s\">%s</a>' % (sin[s:e], sin[s:e])
        sin = '%s%s%s' % (sin[:s], newtext, sin[e:])
        mo = URLRE.search(sin, s + len(newtext))

    return sin

def render(request, entry, template):
    """
    Takes a given request and summarizes it given the registry-template
    template for this flavour.
    """
    config = request.getConfiguration()
    data = request.getData()
    flavour = data.get("flavour", "html")
    renderer = data["renderer"]

    vars = renderer.getParseVars()
    vars.update(entry)
    vars["registry::url"] = urlme

    return renderer.renderTemplate(vars, "registry-%s" % template)


def cb_date_head(args):
    request = args["request"]
    data = request.getData()

    if data.has_key(INIT_KEY):
        args["template"] = ""
    return args

def cb_story(args):
    entry = args["entry"]
    if not entry.has_key("registry_render"):
        entry["registry::url"] = urlme
        return args

    request = args["request"]
    body = entry["registry_render"]
    body = "".join([render(request, m[0], m[1]) for m in body])
    entry["body"] = body
    entry["registry::url"] = urlme

    return args

def generate_entry(request, output, title="Registry", filename="", mtime=None):
    """
    Takes a bunch of text and generates an entry out of it.  It creates
    a timestamp so that conditionalhttp can handle it without getting
    all fussy.
    """
    global CONTRIB_DESC
    entry = base.EntryBase(request)
    registrydir = request.getConfiguration()["registry_dir"]

    entry['title'] = title
    entry['fn'] = filename

    if filename:
        b = TRIGGER[1:]
        f = filename[len(registrydir):-4]
        entry['fn'] = os.path.split(f)[1]
        entry['file_path'] = b + f
        entry['absolute_path'] = b + os.path.split(f)[0]
        entry._id = filename
    else:
        entry["nocomments"] = 1

    if mtime:
        entry.setTime(time.localtime(mtime))
    else:
        entry.setTime(time.localtime())

    entry.setData(output)
    return entry

def fix(s):
    return s.replace("<br>", " ").replace("<", "&lt;").replace(">", "&gt;")

def get_entries(request, registrydir, entries):
    items = [fileentry.FileEntry(request, m, registrydir, registrydir) for m in entries]
    for mem in items:
        desc = mem["body"]
        if len(desc) > 200:
            desc = desc[:200] + "..."

        mem["body"] = fix(mem["body"])
        mem["short_body"] = fix(desc)
    return items
 
def get_entries_by_item(request, registrydir, entries, sortbyitem):
    """
    Takes in a list of filenames for all the entries in a registry and
    returns the listing ordered by the item.
    """
    sortbyitem = "absolute_path"

    request.data["bl_type"] = "dir"
    items = get_entries(request, registrydir, entries)

    items.sort(lambda x,y: cmp(x[sortbyitem] + x.get("title"), 
                               y[sortbyitem] + y.get("title")))

    entries = []
    output = []
    item = ""
    for mem in items:
        if item == "":
            item = mem.get(sortbyitem, "none")

        elif mem.get(sortbyitem, "none") != item:
            entry = generate_entry(request, "", item, item + "." + sortbyitem)
            entry["registry_render"] = output
            entry["template_name"] = "registry-index"
            entry["nocomments"] = 1
            entries.append(entry)

            output = []
            item = mem.get(sortbyitem, "none")

        output.append( (mem, "summary") )

    if output:
        entry = generate_entry(request, "", item, item + "." + sortbyitem)
        entry["registry_render"] = output
        entry["template_name"] = "registry-index"
        entry["nocomments"] = 1
        entries.append(entry)

    return entries

def cb_filelist(args):
    global registrydir, TRIGGER
    request = args["request"]

    pyhttp = request.getHttp()
    data = request.getData()
    config = request.getConfiguration()
    form = pyhttp["form"]

    if not pyhttp["PATH_INFO"].startswith(TRIGGER):
        return

    data[INIT_KEY] = 1

    data['root_datadir'] = config['datadir']

    # if they haven't add a registrydir to their config file, 
    # we pleasantly error out
    if not config.has_key("registry_dir"):
        output = "<p>\"registry_dir\" config setting is not set.  Refer to documentation.</p>"
        return [generate_entry(request, output, "setup error")]

    registrydir = config["registry_dir"]

    # make sure the registrydir has a / at the end
    if registrydir[-1] != os.sep:
        registrydir = registrydir + os.sep

    pathinfo = pyhttp["PATH_INFO"]

    dir2 = pathinfo[len(TRIGGER):]
    if dir2.startswith("/"):
        dir2 = dir2[1:]

    filename, ext = os.path.splitext(dir2)
    fullpath = os.path.join(registrydir, filename)

    if os.path.isdir(fullpath):
        entries = tools.Walk(request, fullpath)

    elif fullpath.endswith("index") and os.path.isdir(fullpath[:len("index")]):
        entries = tools.Walk(request, fullpath[:-1 * len("index")])

    else:
        fext = tools.what_ext(data["extensions"].keys(), fullpath)
        entries = [fullpath + "." + fext]

    if ext[1:]:
        data["flavour"] = ext[1:]

    # that entry doesn't exist....
    if len(entries) == 0:
        output = "<p>No entries of that kind registered here.</p>"
        return [generate_entry(request, output)]
        
    # if we're looking at a specific entry....
    if len(entries) == 1:
        try:
            entry = fileentry.FileEntry(request, entries[0], registrydir, registrydir)
            if entries[0].find("/flavours/") != -1:
                entry["template_name"] = "flavour-story"
            else:
                entry["template_name"] = "registry-story"

            if entry.has_key("contrib"):
                entry["body"] = entry["body"] + CONTRIB_DESC

            return [entry]

        except Exception, e:
            output = "<p>That plugin does not exist.</p>"
            return [generate_entry(request, output)]

    return get_entries_by_item(request, registrydir, entries, "path")
