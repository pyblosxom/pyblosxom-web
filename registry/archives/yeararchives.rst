yeararchives
#author Will Kahn-Greene
#email willg at bluesock dot org
#infourl http://pyblosxom.bluesock.org/
#download None
#summary Builds year-based archives listing.
#license MIT
#registrytags 1.4, 1.5, core
#generator update_registry

Summary
=======

Walks through your blog root figuring out all the available years for
the archives list.  It stores the years with links to year summaries
in the variable ``$archivelinks``.  You should put this variable in either
your head or foot template.


Usage
=====

When the user clicks on one of the year links (i.e. http://base_url/2004/),
then yeararchives will display a summary page for that year.  The summary is
generated using the ``yearsummarystory.html`` template for each month in the
year.  Mine is::

   <div class="blosxomEntry">
   <span class="blosxomTitle">$title</span>
   <div class="blosxomBody">
   <table>
   $body
   </table>
   </div>
   </div>


The ``$(archivelinks)`` link can be configured with the
``archive_template`` config variable.  It uses the Python string
formatting syntax.

Example::

    py['archive_template'] = '<a href="%(base_url)s/%(Y)s/index.%(f)s">%(Y)s</a><br />'

The vars available with typical example values are::

    Y      4-digit year   ex: '1978'
    y      2-digit year   ex: '78'
    f      the flavour    ex: 'html'
