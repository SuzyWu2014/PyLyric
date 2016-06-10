# import os
# import sys
# import time
# import copy
import urllib
import apiError
import urllib2  # needed for the TIMEOUT option, otherwise urllib is enough
# try:
#     from Queue import PriorityQueue, Empty
# except ImportError:
#     from queue import PriorityQueue, Empty
try:
    import json
except ImportError:
    import simplejson as json


MUSIXMATCH_API_ROOT_URL = "http://api.musixmatch.com/ws/1.1/"
MUSIXMATCH_API_KEY = "2ea62062410e6d3f820561245af97ba7"
MAX_CALL_TIMEOUT = 30  # seconds


def call(method, params):
    """
    Do the GET call to the MusixMatch API
    Parameters
        method: string - describe api method, e.g. track.get
        params: dictionary of params, e.g. track_id: 15953433
    """
    params.update({'format': 'json', 'apikey': MUSIXMATCH_API_KEY})
    for key, value in params.items():
        if isinstance(value, unicode):
            params[key] = value.encode('utf-8')
    params = urllib.urlencode(params)

    url = '%s%s?%s' % (MUSIXMATCH_API_ROOT_URL, method, params)
    request = urllib2.urlopen(url, timeout=30)
    response = decode_json(request.read())
    check_rst = apiError.check_status(response)
    return check_rst


def decode_json(raw_json):
    """
    Transform the json into a python dictionary
    or raise a ValueError
    """
    try:
        response_dict = json.loads(raw_json)
    except ValueError:
        raise apiError.MusixMatchAPIError(-1, "Unknown error")
    return response_dict


rst = call("track.lyrics.get", {'track_id': 15445219})

print rst
