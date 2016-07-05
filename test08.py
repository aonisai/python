# -*- coding: utf-8 -*-

import datetime

if __name__ == "__main__":

    today = datetime.datetime.today()

    # date
    print today

    # date of tomorrow
    print today + datetime.timedelta(days=1)

    newyear = datetime.datetime(2010,1,1)

    print newyear
    print newyear + datetime.timedelta(days=7)

    calc = today - newyear

    print calc.days