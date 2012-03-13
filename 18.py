#
#  18.py
#  PythonChallenge
#
#  Created by Jay Roberts on 2012-03-13.
#

# http://www.pythonchallenge.com/pc/return/balloons.html
# huge:file

import os
import urllib

if not os.path.isfile('balloons.jpg'):
    webfile = urllib.urlopen('http://www.pythonchallenge.com/pc/return/balloons.jpg')

    localfile = open('balloons.jpg', 'w')
    localfile.write(webfile.read())
    localfile.close()

# TODO
# Load up balloons.jpg, split each side into A and B
# Subtract B from A
