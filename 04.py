# 
#  4.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-09-29.
# 

# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib
import re  # We learn from the previous lesson

endpoint = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
number = '12345' # <-- Start here
# number = str(92118 / 2)

while True:
    content = urllib.urlopen(endpoint + number).read()
    print content
    number = re.findall('\d+', content)[-1] # Only grab the last matched number, those sneaky...
    print number

print content