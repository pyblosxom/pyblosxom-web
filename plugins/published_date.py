"""
This takes a #published date/time stamp in the entry and returns
that as the mtime.

Example entry::

   My first post!
   #published 2008-01-01 12:20:22
   <p>
     This is my first post!
   </p>

returns an mtime of 01-01-2008 at 12:20:22.

This is released into the public domain.
"""

import time, stat

def get_date(fn):
    f = open(fn, "r")
    lines = f.readlines()
    for line in lines:
        if line.startswith("#published"):
            d = line.split(" ", 1)[1].strip()
            d = time.strptime(d, "%Y-%m-%d %H:%M:%S")
            return tuple(d)

    return None
            
def cb_filestat(args):
    req = args["request"]
    filename = args["filename"]
    mtime = args["mtime"]

    d = get_date(filename)
    if d:
        if len(d) == 9:
            mtime = list(mtime)
            mtime[stat.ST_MTIME] = time.mktime(d)
            mtime = tuple(mtime)

    args["mtime"] = mtime
    return args
