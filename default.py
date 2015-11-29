#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import urllib2
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

channels = json.load(urllib2.urlopen('http://piserver:5555/channels'));

for channel in channels:
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=channel['url'], listitem=xbmcgui.ListItem(channel['name'], iconImage=channel['icon']))		

xbmcplugin.endOfDirectory(addon_handle)