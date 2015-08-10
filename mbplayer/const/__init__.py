# -*- coding: utf-8 -*-

#############################################################################
##
## Copyright (C) 2015 Jim Duke
## All rights reserved.
##
## This file is part of MusicBrainz Player.
##
## MusicBrainz Player is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by the
## Free Software Foundation, either version 3 of the License, or (at your
## option) any later version.
##
## MusicBrainz Player is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
## or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
## for more details.
##
## You should have received a copy of the GNU General Public License along
## with MusicBrainz Player.  If not, see <http://www.gnu.org/licenses/>
##
#############################################################################

import os
import sys

# Install gettext "noop" function in case const.py gets imported directly.
import __builtin__
__builtin__.__dict__['N_'] = lambda a: a

# Config directory
if sys.platform == "win32":
    USER_DIR = os.environ.get("APPDATA", "~\\Application Data")
else:
    USER_DIR = os.environ.get("XDG_CONFIG_HOME", "~/.config")

USER_DIR = os.path.join(
    os.path.expanduser(USER_DIR), "MusicBrainz", "Player"
)

###############################################################################
#
# Reinstate this once we're hooking to AcoustID.  At this time the application
# isn't registered.  Before reinstating this a new KEY will need to be obtained
# by registering this application with AcoustID.
#
###############################################################################
#
## AcoustID client API key
#ACOUSTID_KEY = 'tPrbdkhM'
#ACOUSTID_HOST = 'api.acoustid.org'
#ACOUSTID_PORT = 80
#FPCALC_NAMES = ['fpcalc', 'pyfpcalc']

###############################################################################
#
# Reinstate this once we're hooking to MusicBrainz.  At this time the
# application isn't registered.  Before reinstating this a new ID and SECRET
# must be ontained by registering this application with MusicBrainz.
#
###############################################################################
#
## MB OAuth client credentials
#MUSICBRAINZ_OAUTH_CLIENT_ID = 'ACa9wsDX19cLp-AeEP-vVw'
#MUSICBRAINZ_OAUTH_CLIENT_SECRET = 'xIsvXbIuntaLuRRhzuazOA'

# Cover art archive URL and port
CAA_HOST = "coverartarchive.org"
CAA_PORT = 80

# URLs
#PICARD_URLS = {
#    'documentation':    "http://picard.musicbrainz.org/docs/",
#    'troubleshooting':  "http://picard.musicbrainz.org/docs/troubleshooting/",
#    'home':             "http://picard.musicbrainz.org/",
#    'doc_options':      "http://picard.musicbrainz.org/docs/options/",
#    'plugins':          "http://picard.musicbrainz.org/plugins/",
#    'forum':            "http://forums.musicbrainz.org/viewforum.php?id=2",
#    'donate':           "http://metabrainz.org/donate",
#    'chromaprint':      "http://acoustid.org/chromaprint#download",
#    'acoustid_apikey':  "http://acoustid.org/api-key",
#    'doc_cover_art_types': "http://musicbrainz.org/doc/Cover_Art/Types",
#}

# Various Artists MBID
VARIOUS_ARTISTS_ID = '89ad4ac3-39f7-470e-963a-56509c546377'

# Special purpose track titles
SILENCE_TRACK_TITLE = '[silence]'
DATA_TRACK_TITLE = '[data track]'

# Release formats
#from picard.const.attributes import MB_ATTRIBUTES
#RELEASE_FORMATS = {}
#RELEASE_PRIMARY_GROUPS = {}
#RELEASE_SECONDARY_GROUPS = {}
#for k, v in MB_ATTRIBUTES.iteritems():
#    if k.startswith(u'DB:medium_format/name:'):
#        RELEASE_FORMATS[v] = v
#    elif k.startswith(u'DB:release_group_primary_type/name:'):
#        RELEASE_PRIMARY_GROUPS[v] = v
#    elif k.startswith(u'DB:release_group_secondary_type/name:'):
#        RELEASE_SECONDARY_GROUPS[v] = v

# Release countries
#from picard.const.countries import RELEASE_COUNTRIES

# List of available user interface languages
#from picard.const.languages import UI_LANGUAGES

# List of alias locales
#from picard.const.locales import ALIAS_LOCALES

# List of official musicbrainz servers - must support SSL for mblogin requests (such as collections).
MUSICBRAINZ_SERVERS = [
    'musicbrainz.org',
    'beta.musicbrainz.org',
]
