#! /usr/bin/python
# -*- coding: utf-8 -*-

import paramiko
import sys

hostname = '192.168.0.254'
passwd = 'toor'
port =22
user = 'root'

try:
    con = paramiko.SSHClient()
    con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    con.connect(hostname=hostname, port=port, username=user, password=passwd)
except:
    print("error")
finally:
    con.close()