magicword
#author Nathaniel Gray
#email n8gray /at/ caltech /dot/ edu
#infourl http://pyblosxom.bluesock.org/
#download None
#summary Magic word method for reducing comment spam
#license MIT
#registrytags 1.4, 1.5, core
#generator update_registry

Summary
=======

This is about the simplest anti-comment-spam measure you can imagine, but it's
probably effective enough for all but the most popular blogs.  Here's how it 
works.  You pick a question and put a field on your comment for for the answer 
to the question.  If the user answers it correctly, his comment is accepted.  
Otherwise it's rejected.  Here's how it works:


Setup
=====

First off, this requires the comments plugin to be installed.

Here's an example of what to put in config.py::

    py['mw_question'] = "What is the first word in this sentence?"
    py['mw_answer'] = "what"

Note that mw_answer must be lowercase and without leading or trailing 
whitespace, even if you expect the user to enter capital letters.  Their input
will be lowercased and stripped before it is compared to mw_answer.

Here's what you put in your comment-form.html file::

    The Magic Word:<br />
    <i>$mw_question</i><br />
    <input maxlenth="32" name="magicword" size="50" type="text" /><br />

It's important that the name of the input field is exactly "magicword".


Security note
=============

In order for this to be secure(ish) you need to protect your
``config.py`` file.  This is a good idea anyway!

If your ``config.py`` file is in your web directory, protect it from
being seen by creating or modifying a ``.htaccess`` file in the
directory where ``config.py`` lives with the following contents::

    <Files config.py>
    Order allow,deny
    deny from all
    </Files>

This will prevent people from being able to view ``config.py`` by
browsing to it.
