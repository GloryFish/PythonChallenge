# 
#  7.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-09-30.
# 

import urllib
from PIL import Image
import string

webfile = urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png')

localfile = open('oxygen.png', 'w')
localfile.write(webfile.read())
localfile.close()

i = Image.open('oxygen.png')

halfway = i.size[1] / 2

# The more I do these, the more I like writing list comeprehensions, however I really don't think they are readable for
# people who are new to python
letters = [chr(i.getpixel((x * 7, halfway))[0]) for x in range(0, i.size[0] / 7)]

print string.join(letters, '')

values = [105, 110, 116, 101, 103, 114, 105, 116, 121]

#  Now this one I like
letters = [chr(val) for val in values]

print string.join(letters, '')

