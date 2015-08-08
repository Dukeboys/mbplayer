Key MBPlayer Concepts
=====================

Central repository, local repository, and synchronization
---------------------------------------------------------

This idea was largely influenced the a movie collection application I
own MyMovies (`www.mymovies.dk <http://www.mymovies.dk>`__). The
MyMovies server maintains a community maintained database of DVD and
Blueray metadata not that different from Musicbrainz. Their client
creates a local database that keeps all the information about your
collection. The normal way in which a person adds to the central
database is to modify the metadata on their local database; and during
an optional synchronization process, the user has the option to submit
their changes to the central database. Submissions to the central
database undergo a review process before they're fully available. Again,
not unlike Musicbrainz. The model works very well. The approach also
allows for "Private" items that should never be submitted to a public
server to benefit from the rich metadata model the Musicbrainz offers.

It's also a bit like the GIT model of version control. In the GIT model
the user can commit changes to their local repository as often as they
like. As the user desires, changes made to the local repository can be
pushed to the central repository. The local repository and the remote
repository can deviate from one another and be brought back into sync;
all fully controlled.

Collection, Music Store, and Quarantine
---------------------------------------

Some definitions:

-  **Collection** A collection is the database describing all the music
   you have in your collection and all the various metadata associated
   with that collection. It is an amplified subset of the central
   MusicBrainz database limited to those data directly or indirectly
   related to music in your possession. Your collection is mapped to
   your actual music by maintaining a mapping of MusicBrainz tracks to
   tracks held in one or more Music Stores. It's possible for a track in
   the Collection to map to a track in zero, one, or multiple Music
   Stores. A track might be in your collect but not have any tracks in
   one of your Music Stores because you have an incomplete album. A
   track might have multiple copies in various Music Stores because you
   want to store copies on different media, possibly in different
   formats.

-  **Music Store** A Music Store is an abstract storage interface for
   storing, retrieving, and organizing Tracks and other media in. It is
   backed by an abstract File Store; which provides a simple
   Filesystem-like interface to a variety of storage media; including
   local filesystem, network filesystem, disconnected filesystems, and
   cloud storage systems. Each Music Store has an organization and
   content policy that controls how the various tracks and associated
   media (cover art) are stored and managed it. It covers such aspects
   as File Format, required Metadata tags, naming conventions, directory
   structures and so forth.

-  **Quarantine** When music media are first imported into MusicBrainz
   Player they undergo a process to match them with MusicBrainz entries.
   Until they are positively tagged, they are kept in Quarantine - a
   special Music Store used for all untagged, or otherwise suspect media
   files.

Plugin Architecture
-------------------

I've always liked the concept of a plugin architecture. I'm particularly
fond of those architectures where there is a small core on top of which
the bulk of the application is built using plugins. Much of beets is
structured in this way. Details of the plugin architecture for
MusicBrainz Player will be detailed in [[Plugin Architecture]]
