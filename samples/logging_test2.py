#! /usr/bin/python
# -*- coding: utf-8 -*-

from logging import getLogger, StreamHandler, WARNING, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(WARNING)
logger.setLevel(WARNING)
# handler.setLevel(DEBUG)
# logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

logger.debug("hello")