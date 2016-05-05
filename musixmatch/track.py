"""-------------------------------------------
Query MusixMatch regarding a track
--------------------------------------------"""

"""
TRACK.SEARCH - PARAMETERS
	q					Search within track titles,artists,lyrics
	q_lyrics			Any word in the lyrics
	page				Define the page number for paginated results
	page_size			Define the page size for paginated results. Range is 1 to 100.
	f_has_lyrics		When set, filter only contents with lyrics
	f_artist_id			When set, filter by this artist id
	f_music_genre_id	When set, filter by this music category id
	f_artist_mbid		When set, filter by this artist musicbrainz id
	f_lyrics_language	Filter by the lyrics language (en,it,..)
	s_track_rating		Sort by our popularity index for tracks (asc|desc)
	s_artist_rating		Sort by our popularity index for artists (asc|desc)
	quorum_factor		Search only a part of the given query string.Allowed range is (0.1 – 0.9), default is 1 (100%)
	format				Decide the output type (json or xml)
"""


"""
TRACK.LYRICS.GET - PARAMETERS
	track_id	The musiXmatch track id
	track_mbid	The musicbrainz track id
	format	Decide the output type (json or xml)
"""