#! /home/enigma/.pyenv/versions/2.7.13/bin/python
# -*- coding: utf-8 -*-

import pexpect
import sys

pexpect_list = [u"password", u"#", u">", u"$"]

try:
    prc = pexpect.spawn("usr/bin/ssh 192.168.56.161")
    prc.logfile= sys.stdout
    prc.expect("assword:")
    prc.sendline("toor")
    prc.expect("$")
    prc.sendline("ls -l")
    prc.expect("$")
    prc.expect(pexpect.TIMEOUT)
except pexpect.EOF:
    print("eof")
except pexpect.TIMEOUT:
    print("timeout")
except:
    print("error")