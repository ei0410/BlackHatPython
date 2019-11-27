#!/usr/bin/env python

import urllib2

url = "https://google.com"

headers = {}
headers['User-Agent'] = "Googlebot"

request  = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)

print response.read()
request.close()
