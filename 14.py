# 
#  14.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-11-18.
# 

# http://www.pythonchallenge.com/pc/return/italy.html

import urllib
import PIL
from PIL import Image

webfile = urllib.urlopen('http://www.pythonchallenge.com/pc/return/wire.png')

localfile = open('wire.png', 'w')
localfile.write(webfile.read())
localfile.close()

def copy_color(x, y, i, source, dest):
    print "rendering x: %d y: %d from index: %d" % (x, y, i)
    color = source.getpixel((i, 0))
    dest.putpixel((x, y), color)

minx = 0
miny = 0

maxx = 100
maxy = 100

i = 0
maxi = 10000

source = Image.open('wire.png')
image = Image.new('RGBA', (maxx + 1, maxy + 1), "blue")


while i < 9999:
    # Render top row, left to right
    print "TOP"
    for x in range(minx, maxx):
        copy_color(x, miny, i, source, image)
        i = i + 1
    
    miny = miny + 1

    # Render right column, top to bottom
    print "RIGHT"
    for y in range(miny, maxy):
        copy_color(maxx, y, i, source, image)
        i = i + 1
    
    maxx = maxx - 1
    
    # Render bottom row, right to left
    print "BOTTOM"
    for x in range(maxx, minx, -1):
        copy_color(x, maxy, i, source, image)
        i = i + 1
    
    maxy = maxy - 1
    
    # Render left column, bottom to top
    print "LEFT"
    for y in range(maxy, miny, -1):
        copy_color(minx, y, i, source, image)
        i = i + 1
    
    minx = minx + 1

image.save('wire-spiral.png')