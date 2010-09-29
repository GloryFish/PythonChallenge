# 
#  3.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-09-29.
# 

import re

gunkfile = open('3-gunk.txt', 'r')

gunk = gunkfile.read()

regex = '[a-z]+[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]+'

match = re.findall(regex, gunk)

print match