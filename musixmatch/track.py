# -*- coding: utf-8 -*-
import util
import apiError
"""-------------------------------------------
Query MusixMatch regarding a track
--------------------------------------------"""

def search(**args):
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
		quorum_factor		Search only a part of the given query string.Allowed range is (0.1 – 0.9), default is 1
		format				Decide the output type (json or xml)
	"""

	valid_params = ('q', 'q_track', 'q_artist', 'q_track_artist', 'q_lyrics',
			'page', 'page_size', 'f_has_lyrics', 'f_artist_id',
			'f_artist_mbid', 'quorum_factor', 'apikey')
	for k in args.keys():
		if not k in valid_params:
			raise MusixMatchAPIError(-1,'Invalid track search param: '+str(k))
	track_list = list()
	params = dict((k,v) for k, v in args.iteritems() if not v is None)
	body = util.call('track.search',params)
	track_list_dict = body["track_list"]
	print track_list_dict
	return track_list_dict


"""
TRACK.LYRICS.GET - PARAMETERS
	track_id	The musiXmatch track id
	track_mbid	The musicbrainz track id
	format	Decide the output type (json or xml)
"""

search(q='Rick Astley Never Gonna Give You Up')