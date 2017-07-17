#! /usr/bin/python
# -*- coding: utf-8 -*-

import def_scanner
import re


def firstword(line):
    # print line.split()[0]
    print line


def find_cve(line):
    # print re.findall('cve-....-....', line, re.IGNORECASE)
    string_list = re.findall('cve-....-....', line, re.IGNORECASE)
    # print string_list
    return string_list


def remove_room(line):
    removed_list = filter(lambda s: s != '', line)
    print removed_list

# file = open('/home/enigma/temp/cve_note')
file = open('/home/enigma/temp/test')
# def_scanner.scanner(file, find_cve)
def_scanner.scanner(file, remove_room)

