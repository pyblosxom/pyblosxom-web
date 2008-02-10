import os

blogdir = os.path.dirname(__file__)

py = {}

###############
# Start Below #
###############
# If your PyBlosxom installation is in a funky place, uncomment
# this next line and point it to your PyBlosxom installation
# directory.

# What's this blog's title?
py['blog_title'] = "PyBlosxom - main site"

# What's this blog's description (for outgoing RSS feed)?
py['blog_description'] = "PyBlosxom project web-site"

# What's this blog's author name and email?
py['blog_author'] = "PyBlosxom Development Team"

# blog email address
py['blog_email'] = "pyblosxom-users@lists.sourceforge.net"

# What's this blog's primary language (for outgoing RSS feed)?
py['blog_language'] = "en"

# Encoding for output. Default is iso-8859-1.
py['blog_encoding'] = "iso-8859-1"

# Where are this blog's entries kept?
py['datadir'] = os.path.join(blogdir, "entries")
py['flavourdir'] = os.path.join(blogdir, "flavours")

# Where should PyBlosxom log files be kept?
# py['logdir'] = "/home/groups/p/py/pyblosxom/datadir/logs"
py['log_file'] = os.path.join(blogdir, "logs")
py['log_level'] = "debug"

# List of strings with directories that should be ignored (e.g. "CVS")
# ex: py['ignore_directories'] = ["CVS", "temp"]
py['ignore_directories'] = []

# Should I stick only to the datadir for items or travel down the directory
# hierarchy looking for items?  If so, to what depth?
# 0 = infinite depth (aka grab everything), 1 = datadir only, n = n levels down
py['depth'] = 0

# How many entries should I show on the home page?
py['num_entries'] = 10


#############################
# pylist options            #
#############################
py["lists"] = ["users"]
py["list-users-file"] = "pyblosxom_users.dat"
py["list-users-format"] = [ [], [] ]
py["list-users-output"] = '<a href="%(1)s">%(0)s</a> [ %(1)s ]<br />'

###########################
# Optional Configurations #
###########################

# What should this blog use as its base url?
# py['base_url'] = "http://pyblosxom.sourceforge.net/blog"

# Default parser/preformatter. Defaults to plain (does nothing)
#py['parser'] = 'plain'

# Plugin directories:
# You can now specify where you plugins all lives, there are two types
# of plugindirectories, the standard pyblosxom plugins, and the xmlrpc
# plugins.  You can list out as many directories you want, but they
# should only contain the related plugins.
# Example: py['plugin_dirs'] = ['/opt', '/usr/bin']
# py['plugin_dirs'] = ['/home/groups/p/py/pyblosxom/datadir/plugins']
py['plugin_dirs'] = [ os.path.join(blogdir, "plugins") ]

# There are two ways for PyBlosxom to load plugins.  The first is the
# default way which involves loading all the plugins in the lib/plugins
# directory in alphanumeric order.  The second is by specifying a
# "load_plugins" key here.  Doing so will cause us to load only the
# plugins you name and we will load them in the order you name them.
# The "load_plugins" key is a list of strings where each string is
# the name of a plugin module (i.e. the filename without the .py at
# the end).
# ex: py['load_plugins'] = ["pycalendar", "pyfortune", "pyarchives"]
py['load_plugins'] = ["pyinclude", "pystaticfile", "registry", 
                      "wbgarchives", "pylist" ]

# py["staticdir"] = "/home/groups/p/py/pyblosxom/datadir/static"
py["staticdir"] = os.path.join(blogdir, "static")

# py["registry_dir"] = "/home/groups/p/py/pyblosxom/datadir/registry"
py["registry_dir"] = os.path.join(blogdir, "registry")
py["registry_edit"] = 0

py["mediadir"] = "/images/"

# Doing static rendering?  Static rendering essentially "compiles" your
# blog into a series of static html pages.  For more details, read:
# http://wiki.subtlehints.net/moin/PyBlosxom_2fStaticRendering
# 
# What directory do you want your static html pages to go into?
py["static_dir"] = os.path.join(blogdir, "compiled_site")

# What flavours shouldt get generated?
py["static_flavours"] = ["html"]

# What other paths should we statically render?
# This is for additional urls handled by other plugins like the booklist
# and plugin_info plugins.  If there are multiple flavours you want
# to capture, specify each:
# ex: py["static_urls"] = ["/booklist.rss", "/booklist.html"]

# index
static_urls = [ "/index.xml", 
                "/pyblosxom_users.html" ]

# add static files
for mem in os.listdir(os.path.join(blogdir, "static")):
    if mem.endswith(".txt"):
        static_urls.append( "/static/%s.html" % os.path.splitext(mem)[0] )

# add registry files
for root, dirs, files in os.walk(os.path.join(blogdir, "registry")):
    if ".svn" in root:
        continue

    root = root[len(blogdir) + 9:]
    static_urls.append("/registry%s/index.html?sortby=path" % root)
    for mem in files:
        if mem.endswith(".txt"):
            static_urls.append( "/registry%s/%s.html" % (root, os.path.splitext(mem)[0]))

py["static_urls"] = static_urls

# Whether (1) or not (0) you want to create date indexes using month
# names?  (ex. /2004/Apr/01)  Defaults to 1 (yes).
py["static_monthnames"] = 0
# Whether (1) or not (0) you want to create date indexes using month
# numbers?  (ex. /2004/04/01)  Defaults to 0 (no).
py["static_monthnumbers"] = 1
