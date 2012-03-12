# 
#  12.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-11-18.
# 

# http://www.pythonchallenge.com/pc/return/evil.html
# huge:file

import urllib

webfile = urllib.urlopen('http://www.pythonchallenge.com/pc/return/evil2.gfx')

localfile = open('evil2.gfx', 'w')
localfile.write(webfile.read())

webfile.close()
localfile.close()

gfx = open('evil2.gfx', 'r').read()

# Lots of mucking around with a hex editor and looking up
# image file formats and you can make out some jpeg 
# headers in there.

# Break this file up into 5 pieces, by taking a card (byte) 
# from the top and putting it into a pile (file), then the next
# card goes to the next pile and so on...

# I originally had this written out the long way but when I was 
# looking up sequence slicing I learned how to slice stepwise (i::5)
# which is so cool.

[open('image_%d' % i, 'w').write(gfx[i::5]) for i in range(5)]
