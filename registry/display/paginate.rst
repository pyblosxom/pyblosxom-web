paginate
#author Will Kahn-Greene
#email willg at bluesock dot org
#infourl http://pyblosxom.bluesock.org/
#download None
#summary Allows navigation by page for indexes that have too many entries.
#license MIT
#registrytags 1.5, core
#generator update_registry

Summary
=======

Plugin for paging long index pages.  

PyBlosxom uses the num_entries configuration variable to prevent more
than ``num_entries`` being rendered by cutting the list down to
``num_entries`` entries.  So if your ``num_entries`` is set to 20, you
will only see the first 20 entries rendered.

The paginate overrides this functionality and allows for paging.


Setup
=====

To install paginate, do the following:

1. add ``paginate`` to your ``load_plugins`` list variable in your
   config.py file--make sure it's the first thing listed so that it
   has a chance to operate on the entry list before other plugins.
2. add the ``$(page_navigation)`` variable to your head or foot (or
   both) templates.  this is where the page navigation HTML will
   appear.


Here are some additional configuration variables to adjust the 
behavior::

  paginate_count_from
    datatype:       int
    default value:  0
    description:    Some folks like their paging to start at 1--this
                    enables you to do that.

  paginate_previous_text
    datatype:       string
    default value:  &lt;&lt;
    description:    Allows you to change the text for the prev link.

  paginate_next_text
    datatype:       string
    default value:  &gt;&gt;
    description:    Allows you to change the text for the next link.

  paginate_linkstyle
    datatype:       integer
    default value:  1
    description:    This allows you to change the link style of the paging.
                    style 0:  [1] 2 3 4 5 6 7 8 9 ... >>
                    style 1:  Page 1 of 4 >>


That should be it!


.. Note::
   
   This plugin doesn't work with static rendering.  The problem is that 
   it relies on the querystring to figure out which page to show and when 
   you're static rendering, only the first page is rendered.  This will 
   require a lot of thought to fix.

   If you are someone who is passionate about fixing this issue, let me
   know.
