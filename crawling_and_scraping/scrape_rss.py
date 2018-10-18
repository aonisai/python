# -*- coding: utf-8 -*-

from xml.etree import ElementTree

rss = "/home/enigma/temp/crawling_and_scraping/rss2.xml"

tree = ElementTree.parse(rss)
root = tree.getroot()
for item in root.findall('channel/item'):
    title = item.find('title').text
    url = item.find('link').text
    print(url, title)
