#! /usr/bin/python
# -*- coding: utf-8 -*-

import logging
# from _stat import filemode

MYFORMAT = "[%(asctime)s]%(filename)s(%(lineno)d): %(message)s"

logging.basicConfig(
    filename="/home/enigma/git/python/samples/log_test.txt",
    filemode="w",
    format=MYFORMAT,
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.WARNING
)
logging.debug("1, debug")
logging.info("2, information")
logging.warning("3, warning")
logging.error("4, error")
logging.critical("5, critical")
