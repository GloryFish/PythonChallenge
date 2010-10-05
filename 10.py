# 
#  10.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-10-04.
# 

# sequence.txt
# a = [1, 11, 21, 1211, 111221, 

# Google tells me this is a look and say sequence...
# A bit of thinking reveals the pattern 

a = [1, 
     11,
     21, 
     1211, 
     111221, 
     312211, 
     13112221, 
     1112213211,
     312211131221,
     1311223113112211,
     ]


start = 1

# Obviously too long to type by hand, how to generate numbered sequences?

# Can we convert a number to its spoken version:

# This can do it for any sequence of the smae number, pretty straightforward
def lookandsay(start):
   return str(len(str(num))) + str(num)[0]

# How to break a list into contiguous groups?

# searchsearchsearch..BINGO
# http://docs.python.org/library/itertools.html#itertools.groupby

groups = []
uniquekeys = []
for key, group in groupby():
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)