#! /home/enigma/.pyenv/versions/2.7.13/bin/python
# -*- coding: utf-8 -*-

from pexpect import pxssh
import sys

try:
    con = pxssh.pxssh()
    ip = "ip"
    user = "user"
    pw = "PW"

    con.login(server=ip, username=user, password=pw)
    print "success ssh"
    con.sendline("ls -l")
    print con.prompt()
    print con.before
except pxssh.ExceptionPxssh as e:
    print "pxssh error"
    print e
except:
    print "error"