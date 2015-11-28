#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import xbmcgui
import xbmcplugin


addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

channels = json.loads('[{"name": "m1", "url": "http://109.199.57.6/1VlnWLwEJHgJZQBRIWrkUoKxL_uuvLPskLoc=/9179/index.m3u8", "icon": "http://www.mediaklikk.hu/wp-content/uploads/sites/4/2013/11/M1.png"}, {"name": "m2", "url": "http://109.199.57.6/1VlnXfQEJC7PtIe5l-a9NFNT7XqL2X22W4DE=/9180/index.m3u8", "icon": "http://www.mediaklikk.hu/wp-content/uploads/sites/4/2013/11/M2.png"}, {"name": "m4", "url": "http://109.199.57.6/1VlnXfQEJC7PtIe5l-a9NFNT7XqL2X22W4DE=/9180/index.m3u8", "icon": "http://mediaklikk.cms.mtv.hu/wp-content/uploads/sites/4/2015/06/M4_logo.png"} ]')

for channel in channels:
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=channel['url'], listitem=xbmcgui.ListItem(channel['name'], iconImage=channel['icon']))		

xbmcplugin.endOfDirectory(addon_handle)