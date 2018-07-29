#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
from datetime import date, timedelta

path = ""
# first_dir_list = []

# get 30 days ago
onemonth_ago = date.today() - timedelta(days=30)
# print onemonth_ago

# f_list = os.listdir(path)
first_list = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
# first_list = [f for f in f_list if os.path.isdir(os.path.join(path, f))]

first_dir_list = [d for d in first_list if not d.startswith(".")]
print first_dir_list
"""
for f in first_list:
    if not f.startswith("."):
        # pass
        first_dir_list.append(f)
    #else:
    #    first_dir_list.append(f)
"""

for dir in first_dir_list:
    dir = os.path.join(path, dir)
    # print dir

    files_list = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    # print files_list

    for i in files_list:
        time = os.path.getctime(os.path.join(dir, i))
        file_created_time = date.fromtimestamp(time)
        if file_created_time > onemonth_ago:
            print i
        else:
            pass
            # print "false"
            # print i

    # # second_list = os.listdir(dir)
    # # files_list = []
    # for i in second_list:
    #     if os.path.isfile(os.path.join(dir, i)):
    #         time = os.path.getctime(os.path.join(dir, i))
    #         file_created_time = date.fromtimestamp(time)

    #         if file_created_time < onemonth_ago:
    #             print "true"
    #             print os.path.join(dir, i)
    #         else:
    #             print "false"
    #             print os.path.join(dir, i)
            # print key
