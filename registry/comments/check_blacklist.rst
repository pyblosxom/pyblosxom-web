check_blacklist
#author Will Kahn-Greene
#email willg at bluesock dot org
#infourl http://pyblosxom.bluesock.org/
#download None
#summary Rejects comments that contain specified blacklisted words.
#license MIT
#registrytags 1.4, 1.5, core
#generator update_registry

Summary
=======

This works in conjunction with the comments plugin and allows you to
xreduce comment spam by a words blacklist.  Any comment that contains
one of the blacklisted words will be rejected immediately.

This shouldn't be the only way you reduce comment spam.  It's probably
not useful to everyone, but would be useful to some people as a quick
way of catching some of the comment spam they're getting.


Usage
=====

For setup, all you need to do is set the comment_rejected_words
property in your config.py file.  For example, the following will
reject any incoming comments with the words ``gambling`` or ``casino``
in them::

   py["comment_rejected_words"] = ["gambling", "casino"]


The comment_rejected_words property takes a list of strings as a
value.

.. Note::

   There's a deficiency in the algorithm.  Currently, it will match
   substrings, too.  So if you blacklist the word "word", that'll nix
   comments with "word" in it as well as comments with "crossword"
   because "word" is a substring of "crossword".

   Pick your blacklisted words carefully or fix the algorithm!

.. Note::

   This checks all parts of the comment including the ip address of
   the poster.  Blacklisting ip addresses is as easy as adding the ip
   address to the list::

      py["comment_rejected_words"] = ["192.168.1.1", ...]

Additionally, the wbgcomments_blacklist plugin can log when it
blacklisted a comment and what word was used to blacklist it.
Sometimes this information is interesting.  True, "yes, I want to log"
and False (default) if "no, i don't want to log".  Example::

   py["comment_rejected_words_log"] = False
