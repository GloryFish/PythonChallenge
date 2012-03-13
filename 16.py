##  16.py
#  PythonChallenge
# 
#  Created by Jay Roberts on 2012-03-12.
#

# http://www.pythonchallenge.com/pc/return/mozart.html
# huge:file

import urllib
import PIL
from PIL import Image
import os

if not os.path.isfile('mozart.gif'):
    webfile = urllib.urlopen('http://www.pythonchallenge.com/pc/return/mozart.gif')

    localfile = open('mozart.gif', 'w')
    localfile.write(webfile.read())
    localfile.close()

if not os.path.isfile('mozart.png'):
    # Open and re-save the gif as a png
    exit()

img = Image.open('mozart.png')

adjusted = Image.new('RGBA', img.size)

# we'll use this to shift our sequence of colors
def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]

for y in range(0, img.size[1]):
    # get a list of color values
    colors = []
    
    # Find index of pink marker
    marker_index = 0
    for x in range(0, img.size[0]):
        color = img.getpixel((x, y))
        colors.append(color)
        if color == (255, 0, 255):
            marker_index = x
    
    colors = shift(colors, marker_index)
    
    # write the colors to another image
    for x in range(0, img.size[0]):
        adjusted.putpixel((x, y), colors[x])

adjusted.save('mozart-adjusted.png')

# for x in range(0, img.size[0]):
#     for y in range(0, img.size[1]):
#         offset = 0
#         if (y % 2 == 0):
#             offset = 1
#         color = img.getpixel((x, y))
#         imgA.putpixel((x / 2, y / 2 ), color)
# 
