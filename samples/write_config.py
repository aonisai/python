#! /usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser

config = ConfigParser.ConfigParser()

section1 = "development"
config.add_section(section1)
config.set(section1, "host", "localhost")
config.set(section1, "port", 10001)

section2 = "production"
config.add_section(section2)
config.set(section2, "host", "xxx.co.jp")
config.set(section2, "port", 10002)

with open("setting.ini", "w") as file:
    config.write(file)