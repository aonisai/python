# -*- coding: utf-8 -*-

import feedparser

d = feedparser.parse("https://gotcha.alc.co.jp/rss")

# print(d.entries[0].title)

for entry in d.entries:
    print(entry.title, entry.link)
