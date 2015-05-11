#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  tmdb.py
#
#import urllib2, urllib, json
from urllib2 import Request, urlopen
from __main__ import *
logger.logging.debug ("We arrived at tmdb")
headers = {
  'Accept': 'application/json'
}
params = urllib.urlencode({'query': mmmoviename , 'api_key': config.tmdbapi})
request = Request('http://api.themoviedb.org/3/search/movie' +"?" + params)
logger.logging.debug ("opening url: " + 'http://api.themoviedb.org/3/search/movie' +"?" + params)
response_body = urlopen(request).read()
response_body  = json.loads(response_body)
mdbid = response_body['results'][0]['id']

headers = {
  'Accept': 'application/json'
}
params = urllib.urlencode({'api_key': config.tmdbapi})
request = Request('http://api.themoviedb.org/3/movie/' + str(mdbid) +"?" + params)
logger.logging.debug ("opening url :" + 'http://api.themoviedb.org/3/movie/' + str(mdbid) +"?" + params)
response_body = urlopen(request).read()
response_body  = json.loads(response_body)
tagline = response_body['tagline']
mvdbimg = response_body['backdrop_path']
title = response_body['title']
rlsdate = response_body['release_date']
year,month,date = rlsdate.split("-")
#if mvdbimg is not None:
	#print "http://image.tmdb.org/t/p/original" + mvdbimg