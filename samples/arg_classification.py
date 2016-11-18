#! /usr/bin/python
# -*- coding: utf-8 -*-

import os

words = "/home/masakazu-o/test/sum.c"
print(words)

if not os.path.isdir(words):
    print('file name')
else:
    if words[0] == '/':
        print('abusolute path')
    else:
        print('relative path')
