BtlxAutoURL
===========

About
-----

Bitelxux Oct-2016

This is a plugin for trac that automatically expands
words defined in section [btlxautourl] from trac.ini
to the URLs defined.

e.g.

.. code::

  [btlxautourl]
  google = http://www.google.com
  starwars = http://www.starwars.com

Then, all the words "google" and "starwars" will be
rendered automatically as their URLs. Not need any
more of typing [[http://bla.ble.blu|text]]

Installation
------------

Run

python setup.py bdist_egg

And install the .egg generated, either manually or from the admin
interface in trac.

