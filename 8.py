# 
#  8.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-09-30.
# 

# Everythign got much easier when I actually looked at the picture and realized I was using the wrong library

from bz2 import BZ2Decompressor

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

dc = BZ2Decompressor()

print dc.decompress(pw)

