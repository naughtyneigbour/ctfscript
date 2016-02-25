import PIL
from math import ceil

def horizontal_fill(image, palette_position, nb_pixel = 3):
	"""
	Fill anything that is not the color of the given palette position
	for pixel between two pixel of color given by the palette_position.
	"""
	image = image.convert('P')
	new_data = []
	width = image.size[0]
	color_index = -1
	non_color_count = 0
	for i,v in enumerate(image.getdata()):
		new_data.append(v)

		# starting a new line
		if i%width == 0: 
			color_index = -1
			non_color_count = 0
		if v == palette_position:
			if non_color_count != 0 and non_color_count < nb_pixel:
				for j in range(0, non_color_count):
					new_data[color_index+j+1] = palette_position
			color_index = i
			non_color_count = 0
		elif color_index != -1:
			non_color_count += 1
	image.putdata(new_data)
	return image

def get_palette_position_by_usage(image, usage = 0, reverse = False):
	"""
	0 will give the most used color, 1 the second most used, etc.
	use reverse = True parameter so that 0 become the least used, 1 the second least used, etc.
	"""
	image = image.convert('P')
	colors = sorted(image.getcolors(), key=lambda tup: tup[0], reverse=not(reverse))
	return colors[usage][1]

def overwrite_palette(image, f):
	"""
	f is a function which receive the palette position. It must returns a list of three RGB value [0,0,0]
	"""
	image = image.convert('P')
	new_palette = []
	for i in range(0, len(image.getpalette()), 3):
		values = f(i/3)
		if isinstance(values, list) and len(values) == 3:
			new_palette.append(values[0])
			new_palette.append(values[1])
			new_palette.append(values[2])
		else:
			new_palette += get_palette_rgb(i/3)
	image.putpalette(new_palette)
	return image

def get_palette_rgb(image, position):
	"""
	returns a list of three value representing the RGB of the given position in the palette
	"""
	image = image.convert('P')
	return image.getpalette()[position*3:position*3+3]

def extract_letters(image, letter_palette_position = []):
	"""
	try to extract letter of the captcha.
	return a list of image representing each letter
	"""
	image = image.convert('P')
	letters = [] 
	foundletter = False
	inletter = False
	for x in range(image.size[0]): # slice across
		for y in range(image.size[1]): # slice down
			pixel_color = image.getpixel((x,y))
			if pixel_color in letter_palette_position:
				inletter = True
				break
		if foundletter == False and inletter == True: 
			foundletter = True
			start = x

		if foundletter == True and inletter == False: 
			foundletter = False
			end = x
			letters.append(image.crop((start, 0, end, image.size[1])))

		inletter=False 
	
	return letters

def compare_two_image(image1, image2):
	"""
	Compare this image to a PIL.Image object and return the number of pixel that are different.
	"""
	image1 = image1.convert('L')
	image2 = image2.convert('L').resize(image1.size)

	difference = 0
	for x in range(image1.size[0]):
		for y in range(image1.size[1]):
			if image1.getpixel((x,y)) != image2.getpixel((x,y)):
				difference += 1
				
	return difference	

def find_most_fitting_image(image, list_of_images):
	"""
	Compare image to a list of images and determine which one fit the most to image.
	"""
	best = None
	diff = None
	for image2 in list_of_images:
		difference = compare_two_image(image, image2)
		if diff is None or difference < diff:
			best = image2
			diff = difference
	return best
