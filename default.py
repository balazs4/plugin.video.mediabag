#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import urllib2
import urllib
import urlparse
import xbmcgui
import xbmcplugin

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)


base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'movies')

mediaitems = json.load(urllib2.urlopen('http://piserver:5555/media'))

tags = list()

for item in mediaitems:
    for tag in item['tags']:
        tags.append(tag)


mode = args.get('mode', None)

if mode is None:
    for tag in sorted(list(set(tags))):
        url = build_url({'mode': 'folder', 'foldername': tag})
        li = xbmcgui.ListItem(tag, iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

elif mode[0] == 'folder':
    foldername = args['foldername'][0]
    for item in sorted(filter(lambda x: foldername in x['tags'], mediaitems), key=lambda x: x['name'], reverse=True):
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=item['url'], listitem=xbmcgui.ListItem(item['name'], iconImage=item['icon']), isFolder=False)		




xbmcplugin.endOfDirectory(addon_handle)
	