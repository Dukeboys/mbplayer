Based on the vision for MBPlayer the following are the key technologies
needed:

-  Programming Language
-  Database Engine
-  Musicbrainz interface library
-  Media Engine - the thing that plays music
-  Metadata library
-  GUI Framework

Programming Language
====================

| The programming language choices is largely driven by the availability
  of the other components, portability,
| and personal preference. The languages considered were Java, Python,
  and C/C++. I am comfortable programming
| in any of them; and all have many excellent choices available for
  database support, GUI frameworks, Media Library
| support, and Metadata libraries. Ultimately it came down to the fact
  that Musicbrainz Picard, and MusicBrainz Catalog were both written in
  Python tipped the balance in favor of using Python because of the
  prospect of reusing components from those applications. I plan to
  support the Python 3.x branch of things.

Database Engine
===============

Requirements for the database engine are as follows:

-  Solid SQL support
-  Speed
-  Ease of installation
-  Availability on Windows, Linux, and Mac
-  Transaction support
-  Compatible for use with an Open Source program
-  Compatible with the Musicbrainz schema

| For this application, I think the best choice is an embedded database
  engine, and the clear choice for that
| is SQLite. However, for those that want to have a shared database,
  full RDMS programs such as MySQL and PostGRES
| should be supported. So the technical decision here is to use SQLite
  by default; but to support it through an
| abstraction layer and to try to use only those features of the SQL
  language that is fairly broadly supported by
| all three systems.

Musicbrainz interface library
=============================

After investigating various options it seems that
`python-musicbrainzngs <https://github.com/alastair/python-musicbrainzngs>`__
is the future. It looks like it will need some work to meet all the
needs; but it is in a better place than most others. I will probably end
up contributing to this project in order to move things forward in those
areas that are important to MusicBrainz Player.

Media Engine
============

I could go the way of pulling in various different media libraries; but
there are libraries that do that. From my investigations I like
`MPV <http://mpv.io/>`__ given that it's open source, supports all the
platforms I need, and creates an abstraction for specific media types,
and is being actively maintained.

Metadata Library
================

This took a while to find, surprisingly. However, I kept running into
the library "Mutagen" in various tagger tools and once I looked into it
this is obviously the tool to use. Like most of the things that use it,
however, it will probably be wrapped in an abstraction to help it fit in
the application better. `Mutagen Development
Site <https://bitbucket.org/lazka/mutagen>`__

GUI Toolkit
===========

Given that python is the language of choice, the main contenders are:
TKinter, wxPython, PyGTK3, and PyQt. Tkinter is aging and few if any new
projects are using it; but it sticks around to maintain old, but still
useful applications. wxPython seems to have been receiving more
attention lately; but it only support Python 2.x and with no apparent
desire to support Python 3.x. PyGTK3+ seems to treat Windows as a second
class citizen and the development on that platform lags and is buggy
from time to time. That is just a sense I have from a fairly short
examination; so that conclusion may not be fair. PyQt supports Qt 5.x;
and Python 3.x; and is available in an GPL/LGPL form. PyQt5 seems to be
the way to go.
