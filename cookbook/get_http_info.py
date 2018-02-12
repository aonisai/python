#! /usr/bin/python
# -*- coding: utf-8 -*-

import lxml.html
import requests

# target_url = 'http://news.tv-asahi.co.jp/news_politics/articles/000041338.html'
# target_url = 'https://kb.isc.org/article/AA-01502/81/BIND-9.10.5-S2-Release-Notes.html'
target_url = 'http://www.python.org'
target_html = requests.get(target_url).text
root = lxml.html.fromstring(target_html)
string = root.cssselect('#nojs > p ')[0].text_content()
# string = root.cssselect('#news_body > p')[0].text_content()
# string = root.cssselect('#listitem > p')[0].text_content()

print string
