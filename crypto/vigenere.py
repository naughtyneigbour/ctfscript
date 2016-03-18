#!/usr/bin/python2

import sys
from itertools import starmap, cycle                                                           

"""
A case insensitive vigenres tool
"""


 
def encrypt(message, key):                                                                     
 
    # convert to uppercase.                                                                    
    # strip out non-alpha characters.                                                          
    message = filter(lambda _: _.isalpha(), message.upper())                                   
 
    # single letter encrpytion.                                                                
    def enc(c,k): return chr(((ord(k) + ord(c)) % 26) + ord('A'))                              
 
    return "".join(starmap(enc, zip(message, cycle(key))))                                     
 
def decrypt(message, key):                                                                     
 
    # single letter decryption.                                                                
    def dec(c,k): return chr(((ord(c) - ord(k)) % 26) + ord('A'))                              
 
    return "".join(starmap(dec, zip(message, cycle(key)))) 

def main():
	if(len(sys.argv) != 3):
		print("usage: vigenere.py MESSAGE KEY")
		return 1
	message = sys.argv[1].upper()
	key = sys.argv[2].upper()
	print(decrypt(message, key))
	return 0

if __name__ == "__main__":
    sys.exit(main())

