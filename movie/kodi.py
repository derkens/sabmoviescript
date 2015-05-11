#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  kodi.py
#
from __main__ import *
import urllib2
import time
logger.logging.debug ("We arrived at kodi")

kodi_host = config.kodi_host
kodi_port = config.kodi_port

'''
data = {
	"jsonrpc":"2.0",
	"method":"VideoLibrary.GetEpisodes",
	"params":{"sort": {"order": "ascending", "method": "title"}, "filter": {"operator": "contains", "field": "title", "value": epname}, "properties": ["file"]},
	"id" : 1
}
req = urllib2.Request('http://'+kodi_host+':'+kodi_port+'/jsonrpc')
req.add_header('Content-Type', 'application/json')
r2 = urllib2.urlopen(req, json.dumps(data))
r2 = r2.read()
r2 = json.loads(r2)
xbmcepid = r2['result']['episodes'][0]['episodeid']
'''

data = {
	"jsonrpc":"2.0",
	"method":"VideoLibrary.Scan",
	"params":{"directory": move.scanloc },
	"id" : 1
}
req = urllib2.Request('http://'+kodi_host+':'+kodi_port+'/jsonrpc')
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
	req = urllib2.Request('http://'+kodi_host+':'+kodi_port+'/jsonrpc')
	req.add_header('Content-Type', 'application/json')
	r2 = urllib2.urlopen(req, json.dumps(data))
	r2 = r2.read()
	r2 = json.loads(r2)
except:
	logger.logging.debug("Kodi is unreachable")
	pass
if not r2['result']['limits']['total'] == 0:
	fanart = r2['result']['movies'][0]['art']['fanart']
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
	tagline = r2['result']['movies'][0]['tagline']
else:
	logger.logging.debug("Movie not found in Kodi library")
