Pyblosxom 1.5 final released
#published 2011-12-28 20:24:00

Release!
========

It's been a long road for Pyblosxom 1.5.  The first time I said that
PyBlosxom 1.5 was pretty much done was in June of 2009.  That turned
out to be hilariously wrong and development continued for another two
and a half years.

In that period of time, we switched from svn to git and put the
project on Gitorious, we switched bug trackers, we had like 350
commits, we added tests, we started using a wiki, we abandoned the
wiki, we renamed the project, we overhauled the documentation a few
times, we added plugins, we removed plugins, we did the hokey-pokey
and moved the rest of them around a few times, we moved the project to
GitHub, we started using IRC more heavily, we had three release
candidates, and a bunch of other things.

Was Pyblosxom 1.5 worth it?  Definitely---it's a magnificent
improvement over 1.4.3.  I highly recommend upgrading.

For complete details of what's new in 1.5, read the `WHATSNEW section
of the manual <http://pyblosxom.bluesock.org/1.5/whatsnew.html>`_.
Here are some highlights:

1. We changed the name of the project to Pyblosxom.  Down with camel case.
2. Plugins are now part of the package.  When you upgrade Pyblosxom in
   the future, core plugins will automatically get upgraded, too.
   Plugin documentation is now part of the manual.  There are some new
   plugins, some rewritten plugins, and a bunch of plugins have seen
   significant improvements.
3. pyblosxom-cmd is vastly improved.  Creating a new blog is much
   easier than in previous versions.
4. Better crash handling.  Pyblosxom now has a crash page that makes
   it easier to figure out why it's crashing and either fix it or tell
   someone the information they need to know to fix it.
5. Improved documentation.
6. Vastly cleaner code, more tests, and better project infrastructure.
7. More options for static rendering.

Yay for Pyblosxom 1.5!


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
