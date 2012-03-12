# 
#  11.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-10-05.
# 

# http://www.pythonchallenge.com/pc/return/5808.html
# huge:file

import urllib
from PIL import Image
import string

webfile = urllib.urlopen('http://www.pythonchallenge.com/pc/return/cave.jpg')

localfile = open('cave.jpg', 'w')
localfile.write(webfile.read())

webfile.close()
localfile.close()

img = Image.open('cave.jpg')

width = img.size[0]
height = img.size[1]

imgA = Image.new('RGBA', img.size)
imgB = Image.new('RGBA', img.size)


for x in range(0, img.size[0]):
    for y in range(0, img.size[1]):
        offset = 0
        if (y % 2 == 0):
            offset = 1
        color = img.getpixel((x, y))
        imgA.putpixel((x / 2, y / 2 ), color)

imgA.save('imageA.jpg')

# Creeepy!!!