no_old_comments
#author Blake Winton
#email bwinton+blog@latte.ca
#infourl http://example.com/
#download None
#summary Prevent comments on entries older than a month.
#license Public Domain
#registrytags 1.4, 1.5, core
#generator update_registry

Summary
=======

This plugin implements the ``comment_reject`` callback of the comments
plugin.

If someone tries to comment on an entry that's older than 28 days,
the comment is rejected.


Setup
=====

1. copy this file into your plugins directory
2. add "no_old_comments" to the load_plugins list in your config.py
   file
3. if PyBlosxom is not running as a cgi, then you need to restart
   PyBlosxom


Revisions
=========

1.0 - August 5th 2006: First released.
