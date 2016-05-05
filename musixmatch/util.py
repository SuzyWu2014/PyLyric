import os
import sys
import time
import copy
import urllib
import urllib2  # needed for the TIMEOUT option, otherwise urllib is enough
try:
    from Queue import PriorityQueue, Empty
except ImportError:
    from queue import PriorityQueue, Empty
try:
    import json
except ImportError:
    import simplejson as json


MUSIXMATCH_API_ROOT_URL = "http://api.musixmatch.com/ws/1.1/"
MUSIXMATCH_API_KEY = "2ea62062410e6d3f820561245af97ba7"
MAX_CALL_TIMEOUT = 30 # seconds


""" 
Do the GET call to the MusixMatch API
Parameters
	method: string - describe api method, e.g. track.get
	params: dictionary of params, e.g. track_id: 15953433
"""
def call(method, params):
	params.update({'format':'json','apikey':MUSIXMATCH_API_KEY})
	for key,value in params.items():
		if isinstance(value,unicode):
			params[key] = value.encode('utf-8')
	params = urllib.urlencode(params)

	url = '%s%s?%s' % (MUSIXMATCH_API_ROOT_URL,method,params) 
	request = urllib2.urlopen(url, timeout=30)
	response = request.read()
	

call("track.lyrics.get",{'track_id':15445219})
