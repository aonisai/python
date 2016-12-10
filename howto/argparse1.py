#! /usr/bin/python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("square", help="display a square of a given number", type=int)
# parser.add_argument("--verbosity", "-v", type=int, choices=[0, 1, 2], help="increase output verbosity")
parser.add_argument("--verbosity", "-v", help="increase output verbosity", action="count", default=0)
args = parser.parse_args()
answer = args.square**2

# bugfix: replace == with >=
if args.verbosity >= 2:
    print "the square of {} equals {}".format(args.square, answer)
elif args.verbosity >= 1:
    print "{}^2 == {}".format(args.square, answer)
else:
    print answer
