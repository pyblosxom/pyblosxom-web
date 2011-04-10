pyfilenamemtime
#author Tim Roberts
#email 
#infourl http://pyblosxom.bluesock.org/
#download None
#summary Allows you to codify the mtime in the filename.
#license MIT
#registrytags 1.4, 1.5, core
#generator update_registry

If a filename contains a timestamp in the form of
``YYYY-MM-DD-hh-mm``, change the mtime to be the timestamp instead of
the one kept by the filesystem.

For example, a valid filename would be ``foo-2002-04-01-00-00.txt``
for April fools day on the year 2002.  It is also possible to use
timestamps in the form of ``YYYY-MM-DD``.

http://www.probo.com/timr/blog/
