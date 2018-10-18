# -*- coding: utf-8 -*-

import re
from html import unescape

dp_html = "/home/enigma/temp/crawling_and_scraping/sample_dp.html"

with open(dp_html) as f:
    html = f.read()

for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):
    url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)
    url = 'https://gihyo.jp' + url

    title = re.search(r'<p itemprop="name".*?</p>', partial_html).group(0)
    title = title.replace('<br/>', ' ')
    title = re.sub(r'<.*?>', '', title)
    title = unescape(title)

    print(url, title)
