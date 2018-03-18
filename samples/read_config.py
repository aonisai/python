#! /usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser

config = ConfigParser.ConfigParser()
config.read("setting.ini")

section1 = "development"
print config.get(section1, "host")
print config.get(section1, "port")

if config.has_section("production"):
    section2 = "production"
    if config.has_option(section2, "host"):
        print config.get(section2, "host")
    print config.get(section2, "port")

# print config.has_section("production")
# print config.has_section("staging")

# print config.has_option("production", "host")
# print config.has_option("production", "user")

if config.has_section("development"):
    for dev_i, dev_j in config.items("development"):
    # for dev_i in config.options("development"):
        print "[", dev_i, ":", dev_j, "]"
print config.options("development")
print config.items("development")