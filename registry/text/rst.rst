rst
#author Sean Bowman
#email sean dot bowman at acm dot org
#infourl http://pyblosxom.bluesock.org/
#download As of PyBlosxom 1.5 rc1, comes with PyBlosxom
#summary restructured text support for blog entries
#license MIT
#registrytags 1.5, core
#generator update_registry

Summary
=======

A reStructuredText entry formatter for pyblosxom.  reStructuredText is
part of the docutils project (http://docutils.sourceforge.net/).  To
use, you need a *recent* version of docutils.  A development snapshot
(http://docutils.sourceforge.net/#development-snapshots) will work
fine.


Install
=======

1. copy this file (``rst.py``) to your plugins directory
2. install docutils
3. add ``rst`` to your ``load_plugins`` config variable


Usage
=====

Blog entries with a ``.rst`` extension will be parsed as restructuredText

You can also configure this as your default preformatter for ``.txt``
files by configuring it in your config file as follows::

   py['parser'] = 'reST'

Additionally, you can do this on an entry-by-entry basis by adding
a ``#parser reST`` line in the metadata section.  For example::

   My Little Blog Entry
   #parser reST
   My main story...


Configuration
=============

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
