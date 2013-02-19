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

3. Move the files from the ``compiled_site`` directory to the pyblosxom.github.com repo where our 
   site is hosted on Github Pages.
  
   If it isn't there, make sure to create an empty .nojekyll file in the root of the repo to prevent
   GH pages form breaking the site. 
   (See: https://help.github.com/articles/files-that-start-with-an-underscore-are-missing )


Questions
================

Ask on the mailing list 

pyblosxom-devel at lists dot sourceforge dot net [subscribe/unsubscribe](http://lists.sourceforge.net/lists/listinfo/pyblosxom-devel)

This mailing list is for developers who want to add/modify/delete functionality in Pyblosxom. Since it revolves around Pyblosxom development, it's also a good place to ask questions about how to build plugins and for advice on working around various plugin development issues. 
