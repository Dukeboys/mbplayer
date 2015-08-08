Description
===========

| The user launches the MBPlayer which initializes itself and prompts
  the user for necessary data if it is not
| configured to run properly.

Actors
======

#. User - the user of the MBPlayer application

Pre-conditions
==============

#. MBPlayer is installed
#. MBPlayer is not running

Post Conditions
===============

#. MBPlayer is up and running

Main Success Scenario
=====================

#. The User launches MBPlayer using an OS appropriate method
#. An MBPlayer splash screen comes up and indicates that initialization
   has started
#. MBPlayer confirms that the MusicBrainz connection information is
   correct, updates the status on the splash
   screen.
#. MBPlayer confirms that a local repository has been initialized and a
   connection has been established with it.
#. MBPlayer confirms that all defined Music Libraries are accessible and
   that there is at least one library
   defined.
#. The splash screen closes and the main screen is displayed with the
   last browser selected.

Variants
========

| 3A: If the MBPlayer MusicBrainz information has not been configured,
  or if an error occurs testing the
|  credentials:

#. MBPlayer displays a Wizard describing the problem
#. MBPlayer presents a form where the user can make adjustments to the
   MusicBrainz settings
#. The User chooses to advance the initialization by pressing "Next"
#. Continue on step 4.

--------------

3B: The system is unable connect to MusicBrainz and the user chooses to
continue without it

#. MBPlayer disables all MusicBrainz dependent features
#. Initialization continues on step 4.

--------------

4A: If the MBPlayer local repository has not been initialized, or cannot
be reached:

#. MBPlayer displays (or continues to display) a Wizard describing the
   problem
#. MBPlayer presents a form where the user can make adjustments to the
   database settings and possibly
   initialize the database.
#. The User chooses to advance the intiialization by pressing "Next"

--------------

5A: If there are problems with any Libraries

#. MBPlayer presents a list of libraries with problems and allows the
   user to make corrections
#. User corrects the problem, deletes the erroneous libraries, or makes
   adjustments to the settings
#. The process continues with step 6.
