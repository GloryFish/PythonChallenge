# 
#  6.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-09-30.
# 

# http://www.pythonchallenge.com/pc/def/channel.html

#  This one required out of the box thinking. After #5 I was ready for some mean-spirited clues,
#  but I spent way too much time mangling the source of the html with zip()
 
import urllib
import zipfile
import tempfile
import re
import string

webfile = urllib.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')

localfile = open('channel.zip', 'w')
localfile.write(webfile.read())

webfile.close()
localfile.close()

archive = zipfile.ZipFile('channel.zip', 'r')

print archive.read('readme.txt')

number = '90052'

comments = []

#  Yay we can reuse the code from #4
while True:
    content = archive.read(number + '.txt')
    comments.append(archive.getinfo(number + '.txt').comment) # collect them all!
    print content
    matches = re.findall('\d+', content)
    if len(matches) == 0:
        break
    number = matches[-1]
archive.close()

print string.join(comments, '')

