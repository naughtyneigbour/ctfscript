#!/usr/bin/env python2
from PIL import Image
import pilutil
import os
import subprocess

#
# first way
#
image = Image.open("captcha.png")
position = pilutil.get_palette_position_by_usage(image, 0)
second_position = pilutil.get_palette_position_by_usage(image, 1)
def overwrite(p):
	if p == position:
		return [8,8,8]
	else:
		return pilutil.get_palette_rgb(image, second_position)
image = pilutil.overwrite_palette(image, overwrite)
image = pilutil.horizontal_fill(image, position) # Fill anything that is between black pixel.
image.save("optimized_captcha1.png")

output = subprocess.check_output(['gocr', 'optimized_captcha1.png'])
print 'gocr: optimized_captcha1.png: {0}'.format(output.rstrip())

#
# second way
#
image = Image.open("captcha.png")
position = pilutil.get_palette_position_by_usage(image, 1)
def overwrite(p):
	if p != position:
		return [0,0,0]
	else:
		return [255,255,255]
image = pilutil.overwrite_palette(image, overwrite)
image = pilutil.horizontal_fill(image, position) # Fill anything that is between black pixel.
image.save("optimized_captcha2.png")

output = subprocess.check_output(['gocr', 'optimized_captcha2.png'])
print 'gocr: optimize_captcha2.png: {0}'.format(output.rstrip())

#
# some example of pilutil.
#

# extract letter from the optimized image
letters = pilutil.extract_letters(image, [1])
# get the diff from two letter
diff = pilutil.compare_two_image(letters[0], letters[0])
# find the best fit for two image (the one that have the most identical pixel)
bestfit = pilutil.find_most_fitting_image(letters[0], letters[2:])
