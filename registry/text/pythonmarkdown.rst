PyBlosxom Python Markdown 2
#author Mako, Sean
#email seanh@lavabit.com
#infourl http://github.com/seanh/PyBlosxom-Python-Markdown-2-Plugin
#download http://github.com/seanh/PyBlosxom-Python-Markdown-2-Plugin
#summary Python Markdown 2.x support for blog entries
#license GPLv3
#registrytags 1.5

Summary
=======

This plugin requires Python Markdown v2.x, which you can download from:

http://www.freewisdom.org/projects/python-markdown/

Extract the ``markdown`` directory from the Python Markdown tarball (the
directory containing ``__init__.py``, not the ``Markdown-2.x.y`` directory) into your
pyblosxom plugins dir alongside this plugin.  Your plugins dir should look like
this::

    plugins/                  <-- your pyblosxom plugins dir
       markdown-plugin.py     <-- this file
       markdown/              <-- the Python Markdown module
       ...                    <-- (any other pyblosxom plugins)

Now any posts with filenames ending in one of these extensions will be passed through
python-markdown:

* .txt
* .text
* .mkdn
* .markdown
* .md
* .mdown
* .markdn
* .mkd
* .mdwn
