#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  move.py
#

from __main__ import *
from distutils.dir_util import copy_tree
import shutil

move = True # False for "dry run"

try:
	title = mm.title
	year = mm.year
except NameError:
	title = tmdb.title
	year = tmdb.year

logger.logging.debug("We arrived at move")
if not move:
	logger.logging.debug("dry run (not really moving stuff)")
newname = title + " (" + year + ")"
logger.logging.info("The new name of the movie is going to be: " + newname)
if sab.cat == "kinderfilms":
	newdir = os.path.join(config.mvloc2, newname)
	scanloc = config.mvloc2
else:
	newdir = os.path.join(config.mvloc, newname)
	scanloc = config.mvloc
logger.logging.debug("making directory " + newdir)
if move:
	os.mkdir (newdir)
if dvd is not None:
	if move:
		copy_tree (movieloc, newdir)
else:
	newloc = os.path.join(newdir + "/" + newname + extension)
	logger.logging.info ("The new location is : " + newloc)
	if move:
		os.rename (movieloc , newloc )
	logger.logging.debug ("We move: " + str(movieloc))
	logger.logging.debug (" to: " + newloc)
	if subloc is not None:
		logger.logging.info("Subtitle file found!..")
		newsubloc = os.path.join(newdir + "/" + newname + ".nl" + subext)
		logger.logging.debug ("We move: "+ subloc)
		logger.logging.debug (" to: "+ newsubloc)
		logger.logging.info ("The subtitle is moved to: " + newsubloc)
		if move:
			os.rename(subloc,newsubloc)
if move:
	 shutil.rmtree(sab.path)
