#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  notify.py
#
from __main__ import *

try:
	pushtitle = mm.title + " (" + mm.year + ")"
	try:
		pushmsg = kodi.tagline
		if kodi.tagline == "":
			pushmsg = mm.genre + "  " + "<a href='http://moviemeter.nl/film/" + mm.id + "'><i>meer...</i></a>"
	except:
		pushmsg = mm.genre + "  " + "<a href='http://moviemeter.nl/film/" + mm.id + "'><i>meer...</i></a>"
except NameError:
	pushmsg = "<i>" + tmdb.tagline + "</i>"
	pushtitle = tmdb.title + " (" + tmdb.year + ")"
	logger.logging.debug ("Pushtitle tmdb:" + pushmsg)
	if tmdb.tagline == "":
		try:
			pushmsg = kodi.tagline
			logger.logging.debug ("Pushtitle kodi:" + pushmsg)
			if pushmsg == "":
				pushmsg = "<i>geen extra info...</i>"
		except NameError:
			pushmsg = "<i>geen extra info...</i>"

if config.use_pushover == 1:
	logger.logging.debug ("Sending Pushover notification...")
	conn = httplib.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
		urllib.urlencode({
			"token": config.mvtoken,
			"user": config.user_key,
			"message": pushmsg,
			"title" : pushtitle.encode('utf-8'),
			"device" : config.push_device,
			"html": "1"
		}), { "Content-type": "application/x-www-form-urlencoded" })
	r = conn.getresponse()
	r = json.loads(r.read())
	if r["status"] == 1 :
		logger.logging.info("Pushover notification sent succesfully")
	else:
		logger.logging.error("Pushover failed with following error" + str(r["errors"]))
if config.use_nma == 1:
	logger.logging.info ("Sending NMA notification...")
	from lib.pynma import pynma
	p = pynma.PyNMA(config.nma_api)
	res = p.push(config.app, pushtitle, pushmsg, 0, 1, config.nma_priority )
	if res[config.nma_api][u'code'] == u'200':
		logger.logging.info ("NMA Notification succesfully send")
	else:
		error = res[config.nma_api]['message'].encode('ascii')
		logger.logging.error ("NMA Notification failed: " + error)
if config.use_pushbullet == 1:
	data = urllib.urlencode({
		'type': 'note',
		'title': pushtitle,
		'body': pushmsg,
		'device_id': config.deviceid,
		'channel_tag': config.channeltag
		})
	auth = base64.encodestring('%s:' % config.ptoken).replace('\n', '')
	req = urllib2.Request('https://api.pushbullet.com/v2/pushes', data)
	req.add_header('Authorization', 'Basic %s' % auth)
	response = urllib2.urlopen(req)
	res = json.load(response)
	if 'error' in res:
		logger.logging.info ("Pushbullet notification failed")
	else:
		logger.logging.error ("Pushbullet notification sent succesfully")
if config.use_email == 1:
	text_file.write(pushmsg + "\n")

else:
	if config.use_email == 1:
		text_file.close()
		logger.logging.info ("Sending Email notification...")
		emailer.SendEmail(pushtitle)
		os.remove("Output.txt")
