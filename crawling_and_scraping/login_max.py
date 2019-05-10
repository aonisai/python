#! /usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

# USER = "test"
# PASS = "pass"

# make session for cookie
session = requests.session()

login_info = {
    "login_id": USER,
    "login_pw": PASS,
    "login": "1"
}

# access login page
url_login = "https://pcmax.jp/pcm/login.php"
try:
    res = session.post(url_login, data=login_info)
except requests.exceptions.RequestException as err:
    print("login error")
    sys.exit(1)

# find attendance
soup = BeautifulSoup(res.text, "html.parser")
a = soup.find(class_="header-nav-a header-nav-a14")
if a is None:
    print("not exist")
    while True:
        val = input("close window. push a button.")
        if val:
            break
    sys.exit(1)
url_attendance = urljoin(url_login, a.attrs["href"])
# print("attendance=", url_attendance)

# access attendance page
try:
    res = session.get(url_attendance)
except requests.exceptions.RequestException as err:
    print(err)
    sys.exit(1)
soup02 = BeautifulSoup(res.text, "html.parser")
a2 = soup02.find(href="login_bonus_6days.php?mode=everyday")
# a2 = soup02.find(href="login_bonus_7days.php?mode=everyday")
if not a2:
    print("not exist attendance link")
    while True:
        val = input("close window. push a button.")
        if val:
            break
    sys.exit(1)

# print(a2.get("href"))
url_attendance_last = urljoin(url_attendance, a2.get("href"))
try:
    res = session.get(url_attendance_last)
except requests.exceptions.RequestException as err:
    print(err)
    sys.exit(1)

# print(res.text)
soup03 = BeautifulSoup(res.text, "html.parser")
a3 = soup03.find_all(id="mileArea")
if not a3:
    print("not exist mileArea")
    sys.exit(1)
for i in a3:
    print(i.text)
