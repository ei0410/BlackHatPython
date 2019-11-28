# -*- coding: utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) <= 1:
    print("usage: python scraping.py http://www.sample.com")
    exit()

url = sys.argv[1]
html = requests.get(url)

try:
    soup = BeautifulSoup(html.text, "html.parser")
    print(soup.title.string)

    intag = soup.find_all("input")
    for tag in intag:
        print(tag)

    """
    img = soup.find_all("img")
    for tag in img:
        print(tag)
    """

except Exception as e:
    print('%s' % (e))