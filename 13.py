# 
#  13.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-11-18.
# 

# http://www.pythonchallenge.com/pc/return/disproportional.html
# huge:file

import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

# Poked around the interface using the REPL at this point.
# Got to listMethods(), phone('5'), "He is not the evil"

#  Lots of head banging on desk...

# Looked back through previous "evil" images.
# evil4.jpg had data but was broken. Hex editor
# reveals that Bert is evil!

print proxy.phone('Bert')

