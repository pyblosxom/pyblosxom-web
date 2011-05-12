rst
#author Sean Bowman
#email sean dot bowman at acm dot org
#infourl http://pyblosxom.bluesock.org/
#download None
#summary restructured text support for blog entries
#license MIT
#registrytags 1.5, core
#generator update_registry

A reStructuredText entry formatter for pyblosxom.  reStructuredText is
part of the docutils project (http://docutils.sourceforge.net/).  To
use, you need a *recent* version of docutils.  A development snapshot
(http://docutils.sourceforge.net/#development-snapshots) will work
fine.

Install docutils, copy this file to your pyblosxom Pyblosxom/plugins
directory, and you're ready to go.  Files with a .rst extension will
be marked up as reStructuredText.

You can configure this as your default preformatter for .txt files by
configuring it in your config file as follows::

   py['parser'] = 'reST'

or in your blosxom .txt file entries, place a '#parser reST' line
after the title of your blog::

   My Little Blog Entry
   #parser reST
   My main story...

There's two optional configuration parameter you can for additional
control over the rendered HTML::

   # To set the starting level for the rendered heading elements.
   # 1 is the default.
   py['reST_initial_header_level'] = 1
  
   # Enable or disable the promotion of a lone top-level section title to
   # document title (and subsequent section title to document subtitle
   # promotion); enabled by default.
   py['reST_transform_doctitle'] = 1
    

.. Note::

   If you're not seeing headings that you think should be there, try
   changing the ``reST_initial_header_level`` property to 0.
