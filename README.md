========
 README
========

Summary
=======

This directory holds all the files that are used to "compile" the web-site.


Requirements
============

This requires the latest PyBlosxom in svn trunk.  We use the web-site to
test out static rendering.


Process
=======

1. Run ``compile.sh``.  Depending on how you have PyBlosxom installed,
   you might need to set the ``PYTHONPATH`` environment variable to
   point to PyBlosxom.

2. Test the site by running ``testserver.py``, going to 
   ``http://localhost:8000/`` and running through the site.

3. Use Unison or something like that to move the files from the
   ``compiled_site`` directory to SourceForge.

   You might need someone with permissions to do this.  SourceForge
   is a minor pain in the ass and it's possible that file permissions
   are screwy.


Questions, et al
================

Talk to Will.
