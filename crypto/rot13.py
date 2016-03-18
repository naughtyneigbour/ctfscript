#!/usr/bin/python2

import string
import sys

if len(sys.argv) != 2:
	print "USAGE: {0} TEXT_TO_ROT13".format(__file__)
	exit(0)

rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
print string.translate(sys.argv[1], rot13)
