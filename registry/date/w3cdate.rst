w3cdate
#author Ted Leung
#email twl at sauria dot com
#infourl http://pyblosxom.bluesock.org/
#download As of PyBlosxom 1.5 rc1, comes with PyBlosxom
#summary Adds a 'w3cdate' variable which is the mtime in ISO8601 format.
#license MIT
#registrytags 1.4, 1.5, core
#generator update_registry

Adds a ``w3cdate`` variable to the head and foot templates which has
the mtime of the first entry in the entrylist being displayed (this is
often the youngest/most-recent entry).


.. Note::

   When adding this plugin to the ``load_plugins`` list, it helps to
   put the plugin early in the list so that the data will be
   available to subsequent plugins.

.. Note::

   You might get better results if you have PyXML installed as part
   of your Python installation.  If you don't, then we fudge the date
   using a home-brew function.


Thanks to Matej Cepl for the hacked iso8601 code that doesn't require
PyXML.
