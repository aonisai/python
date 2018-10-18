# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

tmp = '/home/enigma/temp/crawling_and_scraping/index.html'

with open(tmp) as f:
        soup = BeautifulSoup(f, 'html.parser')

for a in soup.find_all('a'):
    print(a.get('href'), a.text)
