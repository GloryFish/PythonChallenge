# 
#  5.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-09-30.
# 

# http://www.pythonchallenge.com/pc/def/peak.html

# Honestly, I have a problem with this challenge. "peak hell" pronounced out loud does NOT sound like
# "pickle," it sounds like peekle. This made me think of peekl and pecl. I agree with this comment:
# http://www.pythonchallenge.com/forums/viewtopic.php?p=2265
# which suggests adding a slightly more suggestive text clue within the page source.
# 
# Now, the peak in the picture does look a bit like a pickle, so, points for that.

# We then write the following code...

import urllib
import pickle
import string

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

content = urllib.urlopen(url).read()

obj = pickle.loads(content)

# At this point we now have an object that when print()ed, dir()ed, and str()ed looks 
# no better than what we started with.

# This challenge then requires a user to simultaneously be familiar with the unix banner program and run-length encoding
# Which I would argue is somewhat of a stretch for challenge number 5. But, enough grumbling, let's print it all out proper:

for line in obj:
    print string.join([run[0] * run[1] for run in line], '')
