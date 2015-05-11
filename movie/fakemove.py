#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  move.py
#

from __main__ import *
from distutils.dir_util import copy_tree
import shutil
logger.logging.debug("We arrived at move.py")
newname = mm.title + " (" + mm.year + ")"
logger.logging.debug("The new name of the movie is going to be: " + newname)
if sab.cat == "kinderfilms":
	newdir = os.path.join("/storage/kids", newname)
else:
	newdir = os.path.join(config.mvloc, newname)
logger.logging.debug("making directory " + newdir)
#os.mkdir (newdir)
if dvd is not None:
	#copy_tree (movieloc, newdir)
	print dvd
	pass
else:
	newloc = os.path.join(newdir + "/" + newname + extension)
	logger.logging.debug ("The new location is : " + newloc)
	#os.rename (movieloc , newloc )
	logger.logging.debug ("We move "+ movieloc +" to "+ newloc)
	if subloc is not None:
		logger.logging.info("Subtitle file found!..")
		newsubloc = newloc = os.path.join(newdir + "/" + newname + ".nl" + subext)
		logger.logging.debug ("We move "+ subloc +" to "+ newsubloc)
		#os.rename(subloc,newsubloc)
#shutil.rmtree(sab.path)
