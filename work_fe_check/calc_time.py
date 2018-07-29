#! /usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import sched
import time


def def1(name):
    print time.time(), name


now = datetime.now()
now = datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
m = now + timedelta(minutes=1)
# m = datetime(now.year, now.month, now.day, now.hour, 20)
# diff = m - now
diff = now - m
print "diff:", diff
print diff.days

if int(diff.days) >= 0:
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(diff.seconds, 1, def1, ("first", ))
    scheduler.run()
else:
    print "do nothing"
