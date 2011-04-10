acronyms
#author Will Kahn-Greene
#email willg at bluesock dot org
#infourl http://pyblosxom.bluesock.org/
#download None
#summary Marks acronyms and abbreviations in blog entries.
#license MIT
#registrytags 1.5, core
#generator update_registry

Summary
=======

This plugin marks abbreviations and acronyms based on an
acronyms/abbreviations files.

To install, do the following:

1. Add ``acronyms`` to the ``load_plugins`` list variable in your
   config.py file::

       py["load_plugins"] = [... "acronyms"]

2. Create an acronyms file with acronyms and abbreviations in it.

   See below for the syntax.

3. Specify the location of the file with the ``acronyms_file``
   variable in your config.py file.

   The default is ``acronyms.txt`` in the parent directory to your
   datadir.


Usage
=====

When writing a blog entry, just write the acronyms and abbreviations
and they'll be marked up by the plugin in the story callback.

If you're writing an entry that you don't want to have marked up, add
this to the metadata for the entry::

    #noacronyms 1


Building the acronyms file
==========================

The file should be a text file with one acronym or abbreviation
followed by an = followed by the explanation.  The
acronym/abbreviation is a regular expression and can contain regular
expression bits.

An acronym is upper or lower case letters that is NOT followed by a
period.  If it's followed by a period, then you need to explicitly
state it's an acronym.

    <acronym> = explanation
    <acronym> = acronym|explanation

Examples::

    ASCII = American Standard Code for Information Interchange
    CGI = Common Gateway Interface; Computer Generated Imagery
    CSS = Cascading Stylesheets
    HTML = Hypertext Markup Language
    HTTP = Hypertext Transport Protocol
    RDF = Resource Description Framework
    RSS = Really Simple Sindication
    URL = Uniform Resource Locator
    URI = Uniform Resource Indicator
    WSGI = Web Server Gateway Interface
    XHTML = Extensible Hypertext Markup Language
    XML = Extensible Markup Language

This one is explicitly labeled an acronym::

    X.M.L. = acronym|Extensible Markup Language

This one uses regular expression to match both ``UTF-8`` and
``UTF8``::

    UTF\-?8 = 8-bit UCS/Unicode Transformation Format

An abbreviation is a series of characters followed by a period.  If
it's not followed by a period, then you need to explicitly state that
it's an abbreviation.

    <abbreviation> = explanation
    <abbreviation> = abbr|explanation

Examples::

    dr. = doctor

This one is explicitly labeled an abbreviation::

    dr = abbr|doctor

.. Note::

   If the first part is an improperly formed regular expression, then
   it will be skipped.

   You can verify that your file is properly formed by running
   ``pyblosxom-cmd test``.


Styling
=======

Might want to add something like this to your CSS::

    acronym {
        bordor-bottom: 1px dashed #aaa;
        cursor: help;
    }

    abbr {
        bordor-bottom: 1px dashed #aaa;
        cursor: help;
    }


Origins
=======

Based on the Blosxom acronyms plugin by Axel Beckert at
http://noone.org/blosxom/acronyms .
