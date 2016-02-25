#!/bin/bash 

type pip2 >/dev/null 2>&1 || { echo >&2 "Please install pip2.  Aborting."; exit 1; }
type gocr >/dev/null 2>&1 || { echo >&2 "Please install gocr (gnu ocr).  Aborting."; exit 1; }

pip2 install Pillow
