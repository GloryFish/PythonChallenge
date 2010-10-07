# 
#  11.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-10-05.
# 


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
        print x + ' ' + y