# 
#  3.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-09-29.
# 

# http://www.pythonchallenge.com/pc/def/equality.html

import re
import string

gunkfile = open('03-gunk.txt', 'r')

gunk = gunkfile.read()

regex = '[a-z]+[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]+'

match = re.findall(regex, gunk)

print string.join(match, '')