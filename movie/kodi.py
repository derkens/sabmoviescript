#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  kodi.py
#
from __main__ import *
import urllib2
import time
logger.logging.debug ("We arrived at kodi")


data = {
	"jsonrpc":"2.0",
	"method":"VideoLibrary.Scan",
	"params":{"directory": move.scanloc },
	"id" : 1
}
req = urllib2.Request('http://'+config.kodi_host+':'+config.kodi_port+'/jsonrpc')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
response = json.loads(response.read())
logger.logging.info ("Scanning movie to kodi library: " + response['result'])

time.sleep(60)

try:
	data = {
		"jsonrpc":"2.0",
		"method":"VideoLibrary.GetMovies",
		"params":{"sort": {"order": "ascending", "method": "title"}, "filter": {"operator": "contains", "field": "title", "value": mmmoviename}, "properties": ["title", "art", "tagline"]},
		"id" : 1
	}
	req = urllib2.Request('http://'+config.kodi_host+':'+config.kodi_port+'/jsonrpc')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	response = json.loads(response.read())
except:
	logger.logging.exception("Exception: ")
	pass
if not response['result']['limits']['total'] == 0:
	if 'fanart' in response:
		fanart = response['result']['movies'][0]['art']['fanart']
		fanart = urllib.unquote(fanart).decode('utf8')
		fanart = fanart[8:].rstrip("/")
		if sab.cat == "kinderfilms":
			fanartloc = "/storage/xbmc/Fanart/KidsFanart"
		else:
			fanartloc = "/storage/xbmc/Fanart/MovieFanArt"
		fanfile = os.path.join(fanartloc, mmmoviename + ".jpg")
		if not os.path.isfile(fanfile):
			 urllib.urlretrieve(fanart, fanfile)
			 logger.logging.debug("Saving backdrop to:" + fanfile)
	else:
		logger.logging.debug("Kodi library has no backdrop info")
		pass

	tagline = response['result']['movies'][0]['tagline']
else:
	logger.logging.debug("Movie not found in Kodi library")
