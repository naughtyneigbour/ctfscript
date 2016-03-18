#!/usr/bin/python2
import sys
import re

if len(sys.argv) != 2:
	print "This tool use the bacon encoding to parse a sentence with majuscule and minuscule into baabb.. structure."
	print "USAGE: {0} TEXT_TO_ENCODE".format(__file__)
	print ""
	print "EXAMPLE:"
	print "$ {0} VoiCIunESUpeRbereCeTtEcONconteepARunGrouPedArtistEsculinaiRedONTleBOnGoutetlESeNsdeLAcLasSenestlimIteEqUeparLEnombreDEcAlOriesqUilsPeUVEntIngurgiter".format(__file__)
	print "$ BAABB AABBB AABAA AABAB ABABB AAAAA AABBA ABAAA BAABA AAAAB AAAAA AAABA ABBBA ABBAB AAAAA ABBAB AAABB ABAAB AAAAA AAABA ABABA AAABB AAAAA ABBAB ABAAA AABAA ABABB BAABA AAAAA"
	exit(0)

s = re.sub('[^0-9a-zA-Z]+', '*', sys.argv[1])
out = ''

for i in range(0, len(s)):
	if i%5 == 0:
		out += ' '
	c = s[i]
	cint = ord(s[i])
	if cint >= 65 and cint <=90:
		out += 'B'
	else:
		out += 'A'

print out
