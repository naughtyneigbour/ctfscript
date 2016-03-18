#!/usr/bin/python
import sys

def xor(message, key):
	return "".join(chr(ord(a)^int(key)) for a in message)

def main():
	if len(sys.argv) != 3:
		print("usage: xor MESSAGE KEY")
		return 1
	key = sys.argv[1]
	message = sys.argv[2]

	print(xor(sys.argv[1], sys.argv[2]))
	return 0

if __name__ == "__main__":
    sys.exit(main())
