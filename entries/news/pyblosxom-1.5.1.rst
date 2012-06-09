Pyblosxom 1.5.1 released!
#published 2011-12-29 19:22:00
This fixes two issues:

1. manifest was missing README.rst which hosed ``python setup.py install``
2. the WHATSNEW page had the wrong version and date for the 1.5 release

The first is bad and worth putting out a new release.  Sorry about
that.  Many thanks to ntoll who popped on IRC and let us know.


Where to get it
===============

We're pushing PyPI now.  To install Pyblosxom::

    pip install pyblosxom

To upgrade::

    pip install --upgrade pyblosxom


For tarballs, source code, and other things, see the website.


How to get help
===============

If you have any problems, say hi on IRC or send an email to the
pyblosxom-users mailing list.  Details are on `the website
<http://pyblosxom.bluesock.org/>`_.
