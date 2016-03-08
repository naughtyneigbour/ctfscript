#!/usr/bin/python2

import subprocess 
from PIL import ImageSequence, Image
sequence = []

im = Image.open("tv.gif")

# im is your original image
frames = [frame.copy() for frame in ImageSequence.Iterator(im)]

print frames

# MERGE every frame of the gif (png) together
#for i in range (0, 29):
#   for j in range (i+1,30):
#       img1 = frames[i].copy()
#       img2 = frames[j].copy()
#       img2.putalpha(25)
#       img1.paste(img2, (0, 0), img2)
#       imagename = "tmp/"+str(i)+"_"+str(j)+".png"
#       img1.save("tmp/"+str(i)+"_"+str(j)+".png")
#       
#       print output
