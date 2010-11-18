# 
#  14.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-11-18.
# 

import PIL
from PIL import Image

def copy_color(x, y, i, source, dest):
    print "rendering x: %d y: %d from index: %d" % (x, y, i)
    color = source.getpixel((i, 0))
    dest.putpixel((x, y), color)

minx = 0
miny = 0

maxx = 99
maxy = 99

i = 0
maxi = 10000

direction = 'right'

source = Image.open('wire.png')
image = Image.new('RGBA', (maxx + 1, maxy + 1))


while i < 9800:
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