# -*- coding: utf-8 -*-

import datetime

def getToday():

    today = datetime.datetime.today()
    value = (today.year,today.month,today.day)

    return value

if __name__ == "__main__":

    test_tuple = getToday()

    print test_tuple
    print test_tuple[0]
    print test_tuple[1]
    print test_tuple[2]