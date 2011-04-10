pages
#author Will Kahn-Greene
#email willg at bluesock dot org
#infourl http://pyblosxom.bluesock.org/
#download None
#summary Allows you to include non-blog-entry files in your site.
#license MIT
#registrytags 1.4, 1.5, core
#generator update_registry

Usage
=====

A blog consists of blog entries, plus a bunch of pages that exist outside
of the blog structure.  For example, an "About me" page or a "Guestbook"
page.  These last two shouldn't be blog entries.  Well, if they're not
blog entries, then how can you have them in your blog?

This plugin solves that problem.  It allows you to have pages in your
website that aren't blog entries that are served up by PyBlosxom.  These
pages can also have plugins.

It looks for urls like::

   /pages/blah

and pulls up the file ``blah.txt`` [1]_ which is located in the path specified
in the config file as ``pagesdir``.  If no pagesdir is specified, then we
use the datadir.

If the file is not there, it kicks up a 404.

.. [1] The file ending (the ``.txt`` part) can be any file ending that's 
   valid for entries on your blog.  For example, if you have the textile
   entryparser installed, then ``.txtl`` is also a valid file ending.

pages formats the page using the ``pages`` template.
So you need to add a ``pages.html`` file to your datadir (assuming
you're using the ``html`` flavour).  I tend to copy my story flavour
templates over and remove the date/time-related bits.

pages handles evaluating python code blocks.  Enclose python
code in ``<%`` and ``%>``.  The assumption is that only you can edit your 
pages files, so there are no restrictions (security or otherwise).

For example::

   <%
   print "testing"
   %>

   <%
   x = { "apple": 5, "banana": 6, "pear": 4 }
   for mem in x.keys():
      print "<li>%s - %s</li>" % (mem, x[mem])
   %>

The request object is available in python code blocks.  Reference it
by ``request``.  Example::

   <%
   config = request.get_configuration()
   print "your datadir is: %s" % config["datadir"]
   %>


Configuration
=============

``pagesdir``

    Optional.  Defaults to the datadir.

    Example::

        py["pagesdir"] = os.path.join(datadir, "pages")

``pages_trigger``

    Optional.  Defaults to ``pages``.

    This is the url trigger that causes the pages plugin to look for pages.

``pages_frontpage``

    Optional.  Defaults to False.

    If set to True, then pages will show the ``frontpage`` entry for the 
    front page.
