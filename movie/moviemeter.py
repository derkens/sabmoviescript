#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  moviemeter.py
#

import urllib, urllib2, json
from __main__ import *
logger.logging.debug ("We arrived at moviemeter")

url = "http://www.moviemeter.nl/api/film/?"
params = urllib.urlencode({'q': mmmoviename, 'api_key': config.mmapi})
r = urllib2.urlopen(url + params).read()
r = json.loads(r)
id = str(r[0]['id'])
logger.logging.debug ("opening url: "+ url + params)

url = "http://www.moviemeter.nl/api/film/"+id+"&"
params = urllib.urlencode({'api_key': config.mmapi})
r = urllib2.urlopen(url + params).read()
r = json.loads(r)
title = r['display_title'].encode('utf-8')
year = str(r['year'])
imdb = str(r['imdb'])
plot = r['plot'].encode('utf-8')
genre = r['genres'][0]
logger.logging.debug ("opening url: "+ url + params)
logger.logging.info ("Movie title found: " + title)
