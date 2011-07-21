flavourfiles
#author Will Kahn-Greene
#email willg at bluesock dot org
#infourl http://pyblosxom.bluesock.org/
#download As of PyBlosxom 1.5 rc1, comes with PyBlosxom
#summary Serves static files related to flavours (css, js, ...)
#license MIT License
#registrytags 1.5, core, experimental
#generator update_registry

Summary
=======

This plugin allows flavour templates to use file urls that will
resolve to files in the flavour directory.  Those files will then get
served by PyBlosxom.

This solves the huge problem that flavour packs are currently
difficult to package, install, and maintain because static files
(images, css, js, ...) have to get put somewhere else and served by
the web-server and this is difficult to walk a user through.

It handles urls that start with ``/flavourfiles/``, then the flavour
name, then the path to the file.

In the flavour template, use::

    $(base_url)/flavourfiles/$(flavour)/path-to-file

For example::

    <img src="$(base_url)/flavourfiles/$(flavour)/header_image.jpg">

The ``$(base_url)`` will get filled in with the correct url root.

The ``$(flavour)`` will get filled in with the name of the url.  This
allows users to change the flavour name without having to update all
the templates.

.. Note::

    This plugin is essentially a draft and it's missing important
    functionality.  I hope to flesh it out and mature it here, then
    fold the functionality into PyBlosxom core.
