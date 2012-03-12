# 
#  1.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-09-29.

# http://www.pythonchallenge.com/pc/def/map.html

import string

cyphertext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#  First I did it with a for loop, then I turned it into a list comprehension.
#  I think the for loop is more readable.

shifted_letters = [string.ascii_lowercase[(i + 2) % len(string.ascii_lowercase)] for i in range(0, len(string.ascii_lowercase))]
shifted_letters = string.join(shifted_letters, '')

transtable = string.maketrans(string.ascii_lowercase, shifted_letters)

print string.ascii_lowercase
print shifted_letters
print string.translate(cyphertext, transtable)

print string.translate('map', transtable)
