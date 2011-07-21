pyarchives
#author Wari Wahab
#email wari at wari dot per dot sg
#infourl http://pyblosxom.bluesock.org/
#download As of PyBlosxom 1.5 rc1, comes with PyBlosxom
#summary Builds month/year-based archives listing.
#license MIT
#registrytags 1.4, 1.5, core
#generator update_registry

Summary
=======

Walks through your blog root figuring out all the available monthly
archives in your blogs.  It generates html with this information and
stores it in the ``$archivelinks`` variable which you can use in your
head and foot templates.

You can change the format of the output in ``config.py`` with the 
``archive_template`` key.

A config.py example::

    py['archive_template'] = '<li><a href="%(base_url)s/%(Y)s/%(b)s">%(m)s/%(y)s</a></li>'

This displays the archives as list items, with a month number slash
year number, like 06/78.

.. Note::

   If you use " (double-quote) characters in the value, then make sure
   to use ' (single-quote) characters to delimit the value string.


The formatting variables available in the ``archive_template`` are::

    b         'Jun'
    m         '6'
    Y         '1978'
    y         '78'

These work the same as ``time.strftime`` in python.

Additionally, you can use variables from config and data.

.. Note::

   The syntax used here is the Python string formatting syntax---not
   the PyBlosxom template rendering syntax!
