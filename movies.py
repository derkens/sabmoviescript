#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  movies.py
#
#  Copyright 2015 Danny Erkens <derkens@gmail.com>
#
import sys, os, re, httplib, urllib, json
import ConfigParser as configparser
import lib2.config as config
import lib2.logger.logger as logger
import movie.sabvariables as sab


if sab.status is not "0":
	sys.exit()

logger.logging.debug("Category from sabnzbd:" + sab.cat)
if sab.cat == "qoq":
	from movie.getfilesandnames import qoq
	mmmoviename,movieloc,extension,subloc,subext,dvd  = qoq()

if sab.cat == "hannes3":
	from movie.getfilesandnames import hannes3
	mmmoviename,movieloc,extension,subloc,subext,dvd = hannes3()

if sab.cat == "karma":
	from movie.getfilesandnames import karma
	mmmoviename,movieloc,extension,subloc,subext,dvd = karma()

if sab.cat == "films" or sab.cat == "kinderfilms":
	from movie.getfilesandnames import default
	mmmoviename,movieloc,extension,subloc,subext,dvd = default()

#import movie.moviemeter as mm
import movie.tmdb as tmdb
import movie.move as move
import movie.kodi as kodi
import movie.notify as notify
