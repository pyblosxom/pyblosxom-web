pycalendar
#author Will Kahn-Greene
#email willg at bluesock dot org
#infourl http://pyblosxom.bluesock.org/
#download None
#summary Displays a calendar on your blog.
#license MIT
#generator update_registry

Generates a calendar along the lines of this one (with month and day names in
the configured locale)::

    <   January 2003   >
    Mo Tu We Th Fr Sa Su
           1  2  3  4  5
     6  7  8  9 10 11 12
    13 14 15 16 17 18 19
    20 21 22 23 24 25 26
    27 28 29 30 31

It walks through all your entries and marks the dates that have entries
so you can click on the date and see entries for that date.

You can set the start of the week using the ``calendar_firstweekday``
configuration setting, for example::

   py['calendar_firstweekday'] = 0

will make the week start on Monday (day '0'), instead of Sunday (day '6').

Pycalendar is locale-aware.  If you set the "locale" config property,
then month and day names will be displayed according to your locale.

It uses the following CSS classes:

* blosxomCalendar: for the calendar table
* blosxomCalendarHead: for the month year header (January 2003)
* blosxomCalendarWeekHeader: for the week header (Su, Mo, Tu, ...)
* blosxomCalendarEmpty: for filler days
* blosxomCalendarCell: for calendar days that aren't today
* blosxomCalendarBlogged: for calendar days that aren't today that
  have entries
* blosxomCalendarSpecificDay: for the specific day we're looking at
  (if we're looking at a specific day)
* blosxomCalendarToday: for today's calendar day


To use, place ``$calendar`` in your head/foot template.
