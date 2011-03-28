firstdaydiv
#author Blake Winton
#email bwinton@latte.ca
#infourl http://pyblosxom.bluesock.org/
#download None
#summary Adds a token which tells us whether we're the first day being displayed or not.
#license MIT
#generator update_registry

This is my fancy module to add a token which tells us whether we're
the first day being displayed or not.

To install:

1. Copy this file into your pyblosxom/Pyblosxom/plugins directory.

2. Create a file named date_head.html in your datadir containing::

      <div class="$dayDivClass">
      <span class="blosxomDate">$date</span>

3. Edit your config.py and add the line::

      py['firstDayDiv'] = 'blosxomFirstDayDiv'

4. That's it.  You're done.

Questions, comments, concerns?  Email bwinton at latte dot ca for help.
