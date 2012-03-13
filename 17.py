#
#  17.py
#  PythonChallenge
#
#  Created by Jay Roberts on 2012-03-12.
#

# http://www.pythonchallenge.com/pc/return/romance.html
# huge:file

import os
import urllib
import urllib2
import zipfile
import tempfile
import re
import string
import cookielib
import Cookie
import bz2
from bz2 import BZ2Decompressor

# if not os.path.isfile('cookies.jpg'):
#     webfile = urllib.urlopen('http://www.pythonchallenge.com/pc/return/cookies.jpg')
# 
#     localfile = open('cookies.jpg', 'w')
#     localfile.write(webfile.read())
#     localfile.close()
# 
# Lots of head banging here trying to find cookies from this page and attempting to play the image
# using audio modules. /facepalm
#
# Eventually, while reviewing older challenges for clues I recognized the toy on #4 and checked
# the cookies there (I just looked in my browser):
#
# you+should+have+followed+busynothing...

# Update the endpoint from #4...
endpoint = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='

# number = '30777' # This number just looooops around
# number = '67111' # This one too
number = '12345' # This one too...

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

values = {'username': 'huge', 'password': 'file'}
auth = urllib.urlencode(values)

cookies = []
last_count = len(cookies)

if not os.path.isfile('cookies.txt'):
    
    while True:
        content = opener.open(endpoint + number, auth).read()

        cookie = cj._cookies['.pythonchallenge.com']['/']['info']
        cookies.append(cookie.value)
        
        print str(cookie.value)
        print number
        print len(cookies)

        if content != 'that\'s it.':
            number = re.findall('\d+', content)[-1] # Only grab the last matched number, those sneaky...
        else:
            break

        cookiefile = open('cookies.txt', 'w')
        for cookie in cookies:
            cookiefile.write(cookie)
        cookiefile.close()

cookiefile = open('cookies.txt', 'r')
cookies = [line.rstrip("\n") for line in cookiefile.readlines()]

data = ''.join(cookies)

data = urllib.unquote_plus(data) # PLUS PLUS PLUS! Took forever to discover this version of the function. Must read all docs.

print data

print bz2.decompress(data)

# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.

import xmlrpclib
proxy = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print proxy.phone('Leopold')

# cookie = Cookie.SimpleCookie()
# cookie.domain = '.pythonchallenge.com'
# cookie.path = '/'
# cookie.name = 'info'
# cookie.value = 'the flowers are on their way'
# cookie.version = '1'
# cj.set_cookie(cookie)
# 
# content = opener.open('http://www.pythonchallenge.com/pc/stuff/violin.php', auth).read()
# 
# print content
# 
# print cj._cookies['.pythonchallenge.com']['/']['info']

# Couldn't get python to set a cookie so I used Chrome

