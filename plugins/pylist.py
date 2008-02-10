# vim: tabstop=4 shiftwidth=4 expandtab
"""
Pylist takes a plain text file and turns it into a unorderd list that can be
renderd as a part of the blog, for example a list of books you're reading, some
links, a smal image gallery etc.

It is configured with the following variables:

# What lists do we want to render
py['lists'] = ['links','books']

# the linklist consists of entrys on the format:
# <category>::<url>::<title>::<description>
py['list-links-file']   = "links.dat"       # the filename, relative the blog root
py['list-links-format'] = [["GROUP","SORT"],[],[],[]]   # sort and group the entrys
                                            # acording to the category
py['list-links-output'] = "<a href='%(1)s' title='%(3)s'>%(2)s</a>" # The format of each entry
                                            # the format is used with pythons % operator


# A basic booklist.
# <category>::<title>::<author>
py['list-books-file']   = "books.dat"
py['list-books-format'] = [["GROUP","SORT"],[],["GROUP"]]
py['list-books-output'] = "%(1)s"


The basic idea comes from the booklist plugin by Will Guaraldi

"""
import Pyblosxom, os, time
from Pyblosxom.renderers.blosxom import BlosxomRenderer
from Pyblosxom.entries.base import EntryBase
from Pyblosxom.pyblosxom import PyBlosxom

INIT_KEY = "pylist_file_list_initiated"

def new_entry(request, title, mtime, body):
    """
    Takes a bunch of variables and generates an entry out of it.  It creates
    a timestamp so that conditionalhttp can handle it without getting
    all fussy.
    """
    entry = EntryBase(request)

    entry['title'] = title
    entry['filename'] = title + "/list"
    entry['file_path'] = title
    entry._id = title + "::list"

    entry["template_name"] = "list-%s" % title
    entry["nocomments"] = "yes"

    entry.setTime(mtime)
    entry.setData(body)

    return entry

def cb_date_head(args):
    request = args["request"]
    data = request.getData()

    if data.has_key(INIT_KEY):
        args["template"] = ""
    return args

class PyblosxomList:
    def __init__(self, request, l):
        self._request = request
        self._listname = l
        self._list = None
        self._output = None

    def __str__(self):
        if not self._output:
            config = self._request.getConfiguration()
            fn = config.get("list-%s-file" % self._listname,"")
            format = config.get("list-%s-format" % self._listname,[[]])
            output = config.get("list-%s-output" % self._listname,"")

            if not self._list:
                self.fill_list(config["datadir"] + "/" + fn)

            groupby=[]
            curgroup=map(lambda a:None,range(len(format)))
            for i in range(0,len(format)):
                if "GROUP" in format[i]:
                    groupby.append(i)
                if "SORT" in format[i]:
                    self._list.sort(lambda a,b:cmp(a[i],b[i]))

            repr = ["<ul>"]
            for a in self._list:
                for g in groupby:
                    if a[g] <> curgroup[g]:
                        if curgroup[g]:
                            repr.append(" "*g+"</li></ul>")
                for g in groupby:
                    if a[g] <> curgroup[g]:
                        repr.append(" "*g+"<li>%s<ul>"%a[g])
                        curgroup[g] = a[g]

                repr.append(("<li>%s</li>"%output)%dict(map(None,map(str,range(len(a))),a)))
            repr.append("</ul>")
            self._output= "\n".join(repr)

        return self._output

    def fill_list(self, fn):
        f = open(fn, "r")
        lines = f.readlines()
        f.close()

        self._list = []
        for line in lines:
            if line and not line.startswith("#"):
                self._list.append(line.split("::"))

    def mtime(self):
        config = self._request.getConfiguration()
        fn = config["datadir"] + "/" + config.get("list-%s-file" % self._listname,"")
        return time.localtime(os.stat(fn)[8])

    def page(self):
        config = self._request.getConfiguration()
        fn = config.get("list-%s-file" % self._listname,"")
        format = config.get("list-%s-format" % self._listname, [[]])
        output = config.get("list-%s-output" % self._listname, "")

        if not self._list:
            self.fill_list(config["datadir"] + "/" + fn)

        l = self._list

        groupby=[]
        curgroup=map(lambda a:None,range(len(format)))
        for i in range(0,len(format)):
            if "GROUP" in format[i]:
                groupby.append(i)
            if "SORT" in format[i]:
                l.sort(lambda a,b:cmp(a[i],b[i]))

        repr = ["<ul>"]
        for a in l:
            for g in groupby:
                if a[g] <> curgroup[g]:
                    if curgroup[g]:
                        repr.append(" "*g+"</li></ul>")
            for g in groupby:
                if a[g] <> curgroup[g]:
                    repr.append(" "*g+"<li>%s<ul>"%a[g])
                    curgroup[g] = a[g]

            repr.append(("<li>%s</li>"%output)%dict(map(None,map(str,range(len(a))),a)))
        repr.append("</ul>")
        self._output= "\n".join(repr)

        return self._output


def cb_filelist(args):
    """
    A callback to generate a list of L{EntryBase} subclasses.

    If C{None} is returned, then the callback chain will try the next plugin in
    the list.

    @param args: A dict containing a L{Request()} object
    @type args: dict
    @returns: None or list of L{EntryBase}.
    @rtype: list
    """
    request = args["request"]
    config = request.getConfiguration()
    data = request.getData()
    pyhttp = request.getHttp()
    path = pyhttp["PATH_INFO"]

    for l in config.get('lists', []):
        fn = config.get("list-%s-file" % l, "")
        fn = fn.replace(".dat", "")
        if path.startswith("/" + fn):
            pl = PyblosxomList(request, l)
            entry = new_entry(request, l, pl.mtime(), pl.page())
            data[INIT_KEY] = 1
            return [entry]

    return
