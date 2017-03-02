#! /usr/bin/python
# -*- coding: utf-8 -*-

# import sets
# sets　モジュールは無くなっている

# Setはsetに変わっている
# 文字列から重複を削除し２つの比較から重複しているものを抽出
magic_chars = set('abracadabra')
poppins_chars = set('supercalifragilisticexpialidocious')
print ''.join(magic_chars & poppins_chars)
print magic_chars
print poppins_chars

thestring = 'abcdefga'
thelist = list(thestring)
theset = set(thestring)

print thestring
print thelist
print theset

for c in thestring:
    print c
