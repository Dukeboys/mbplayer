# Makefile for the MusicBrainz Player
#

# List of generated files
GENERATED=mbplayer_rc.py

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest coverage gettext

all:	mbplayer_rc.py

mbplayer_rc.py:	mbplayer.qrc qss/*.qss
	pyrcc5 -o mbplayer_rc.py mbplayer.qrc

clean:
	rm -rf $(GENERATED)
