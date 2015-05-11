#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  getfilesandnames.py
#

from __main__ import *
import fnmatch

mmmoviename = None
movieloc = None
extension = None
subloc  = None
subext = None
dvd = None


def qoq():
	global mmmoviename,movieloc,extension,subloc,subext,dvd
	logger.logging.debug("We arrived at getfilesandnames - def qoq()")
	for root, dirs, files in os.walk(sab.path):
		for file in files:
			if file.endswith(".mkv"):
				movieloc = (os.path.join(root, file))
				moviename = os.path.splitext(file)[0][::-1]
				extension = os.path.splitext(file)[1]
				mmmoviename = re.split('.\d\d\d\d.', moviename, 1, 0)[0]
				mmmoviename = mmmoviename.replace(".", " ")
				mmmoviename = mmmoviename.strip()
				return (mmmoviename,movieloc,extension,subloc,subext,dvd)

def hannes3():
	global mmmoviename,movieloc,extension,subloc,subext,dvd
	logger.logging.debug("We arrived at getfilesandnames - def hannes3()")
	for root, dirs, files in os.walk(sab.path):
		for file in files:
			if file.endswith(".avi"):
				movieloc = (os.path.join(root, file))
				moviename = os.path.splitext(file)[0][::-1]
				extension = os.path.splitext(file)[1]
				mmmoviename = re.split('.\d\d\d\d', moviename, 1, 0)[0]
				mmmoviename = mmmoviename.replace(".", " ")
				mmmoviename = mmmoviename.strip()
	hannessubdirs = ['*ut srt', '*l srt']
	for root, dirnames, filenames in os.walk(sab.path):
		for dirs in hannessubdirs:
			for dirname in fnmatch.filter(dirnames, dirs):
				subdir = dirname
	if 'subdir' in locals():
		for root, dirs, files in os.walk(os.path.join(sab.path, subdir)):
			for file in files:
				if file.endswith(".srt"):
					subloc = (os.path.join(root, file))
					subext = os.path.splitext(file)[1]
	return (mmmoviename,movieloc,extension,subloc,subext,dvd)

def karma():
	global mmmoviename,movieloc,extension,subloc,subext,dvd
	logger.logging.debug("We arrived at getfilesandnames - def karma()")
	for root, dirs, files in os.walk(sab.path):
		for file in files:
			if file.endswith(".mkv"):
				movieloc = (os.path.join(root, file))
				moviename = os.path.basename(sab.path)
				mmmoviename = re.split('.\d\d\d\d', moviename, 1, 0)[0]
				mmmoviename = mmmoviename.strip()
				extension = os.path.splitext(file)[1]
				return (mmmoviename,movieloc,extension,subloc,subext,dvd)


def default():
	global mmmoviename,movieloc,extension,subloc,subext,dvd
	logger.logging.debug("We arrived at getfilesandnames - def default()")
	ext = [".avi", ".m2ts", ".mkv", ".mp4", ".mpg", ".mpeg", ".wmv", ".iso", ".ISO"]
	ext2 = [".VOB", ".vob",]
	for root, dirs, files in os.walk(sab.path):
		for file in files:
			if file.endswith(tuple(ext)):
				movieloc = (os.path.join(root, file))
				moviename = os.path.basename(sab.path)
				moviename = moviename.replace(".", " ")
				moviename = moviename.replace("_", " ")
				mmmoviename = re.split('.\d\d\d\d', moviename, 1, 0)[0]
				mmmoviename = mmmoviename.strip()
				if " s " in mmmoviename:
					mmmoviename = mmmoviename.replace(" s", "\'s")
				extension = os.path.splitext(file)[1]
			if file.endswith(tuple(ext2)):
				logger.logging.info("DVD like structure detected...")
				moviename = os.path.basename(sab.path)
				moviename = moviename.replace(".", " ")
				moviename = moviename.replace("_", " ")
				mmmoviename = re.split('.\d\d\d\d.', moviename, 1, 0)[0]
				mmmoviename = mmmoviename.strip()
				movieloc = sab.path
				dvd = "1"
				break
	ext = [".srt", ".sub"]
	for root, dirs, files in os.walk(sab.path):
		for file in files:
			if file.endswith(tuple(ext)):
				subloc = (os.path.join(root, file))
				subext = os.path.splitext(file)[1]
	return (mmmoviename,movieloc,extension,subloc,subext,dvd)
