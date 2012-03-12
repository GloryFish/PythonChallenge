# 
#  2.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-09-29.
# 

# http://www.pythonchallenge.com/pc/def/ocr.html

import string

gunkfile = open('02-gunk.txt', 'r')

gunk = gunkfile.read()

occurances = {}

#  Originally I enumerated the lines in the file, and then enumerated the characters in each line
#  Doing this, I learned that you can just call .read() on a file-like object to enumerate it character-by-character
for char in gunk:
    if char in occurances:
        occurances[char] = occurances[char] + 1
    else:
        occurances[char] = 1

unique = [char for char in occurances.keys() if occurances[char] == 1]

print string.join(unique, '') # My brain can figure out what this is an anagram for