tags
#author Will Kahn-Greene
#email willg at bluesock dot org
#infourl http://pyblosxom.bluesock.org/
#download None
#summary Tags plugin
#license MIT
#generator update_registry

Summary
=======

This is a tags plugin.  It uses PyBlosxom 1.5's command line abilities
to split generation of tags index data from display of tags index
data.

It creates a ``$(tagslist)`` variable for head and foot templates
which lists all the tags.

It creates a ``$(tags)`` variable for story templates which lists tags
for the story.


Configuration
=============

The following config properties define where the tags file is located,
how tag metadata is formatted, and how tag lists triggered.

``tags_separator``

    This defines the separator between tags in the metadata line.
    Defaults to ",".

    After splitting on the separator, each individual tag is stripped
    of whitespace before and after the text.

    For example::

       Weather in Boston
       #tags weather, boston
       <p>
         The weather in Boston today is pretty nice.
       </p>

    returns tags ``weather`` and ``boston``.

    If the ``tags_separator`` is::

       py["tags_separator"] = "::"

    then tags could be declared in the entries like this::

       Weather in Boston
       #tags weather::boston
       <p>
         The weather in Boston today is pretty nice.
       </p>

``tags_filename``

    This is the file that holds indexed tags data.  Defaults to
    datadir + os.pardir + ``tags.index``.

    This file needs to be readable by the process that runs your blog.
    This file needs to be writable by the process that creates the
    index.

``tags_trigger``

    This is the url trigger to indicate that the tags plugin should
    handle the file list based on the tag.  Defaults to ``tag``.


In the head and foot templates, you can list all the tags with the
``$(tagslist)`` variable.  The templates for this listing use the
following three config properties:

``tags_list_start``

    Printed before the list.  Defaults to ``<p>``.

``tags_list_item``

    Used for each tag in the list.  There are a bunch of variables you can
    use:

    * ``base_url`` - the baseurl for your blog
    * ``flavour`` - the default flavour or flavour currently showing
    * ``tag`` - the tag name
    * ``count`` - the number of items that are tagged with this tag
    * ``tagurl`` - url composed of baseurl, trigger, and tag

    Defaults to ``<a href="%(tagurl)s">%(tag)s</a>``.

``tags_list_finish``

    Printed after the list.  Defaults to ``</p>``.


You can list the tags for a given entry in the story template with the
``$(tags)`` variable.  The tag items in the story are formatted with one
configuration property:

``tags_item``

    This is the template for a single tag for an entry.  It can use the
    following bits:

    * ``base_url`` - the baseurl for this blog
    * ``flavour`` - the default flavour or flavour currently being viewed
    * ``tag`` - the tag
    * ``tagurl`` - url composed of baseurl, trigger and tag

    Defaults to ``<a href="%(tagurl)s">%(tag)s</a>``.

    Tags are joined together with ``,``.


Creating the tags index file
============================

Run::

    pyblosxom-cmd buildtags

from the directory your ``config.py`` is in or::

    pyblosxom-cmd buildtags --config=/path/to/config/file 

from anywhere.

This builds the tags index file that the tags plugin requires to
generate tags-based bits for the request.

Until you rebuild the tags index file, the entry will not have its
tags indexed.  Thus you should either rebuild the tags file after writing
or updating an entry or you should rebuild the tags file as a cron job.

.. Note::

   If you're using static rendering, you need to build the tags
   index before you statically render your blog.


Converting from categories to tags
==================================

This plugin has a command that goes through your entries and adds tag
metadata based on the category.  There are some caveats:

1. it assumes entries are in the blosxom format of title, then
   metadata, then the body.

2. it only operates on entries in the datadir.

It maintains the atime and mtime of the file.  My suggestion is to
back up your files (use tar or something that maintains file stats),
then try it out and see how well it works, and figure out if that
works or not.

To run the command do::

    pyblosxom-cmd categorytotags

from the directory your ``config.py`` is in or::

    pyblosxom-cmd categorytotags --config=/path/to/config/file

from anywhere.
