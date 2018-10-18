# -*- coding: utf-8 -*-

import lxml.html

tmp = '/home/enigma/temp/crawling_and_scraping/index.html'

tree = lxml.html.parse(tmp)
html = tree.getroot()

for a in html.cssselect('a'):
    print(a.get('href'), a.text)
