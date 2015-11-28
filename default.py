#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import os
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

addonPath = xbmcaddon.Addon().getAddonInfo("path")
channel_file = os.path.join(addonPath,'resources/data/channels.json')

channels = json.load(open(channel_file));

for channel in channels:
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=channel['url'], listitem=xbmcgui.ListItem(channel['name'], iconImage=channel['icon']))		

xbmcplugin.endOfDirectory(addon_handle)