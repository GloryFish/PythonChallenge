# 
#  15.py
#  PythonChallenge
#  
#  Created by Jay Roberts on 2010-11-18.
# 


import calendar

cal = calendar.TextCalendar(6)

# In our supplied calendar, we don't know what 
# year it is supposed to be. But we do know that, in 
# that year, January starts on a Thursday and we know
# the first and last digets of the year (1, 6).

years = []

for year in range(106, 1996):
    s = str(year)
    if s[0] == '1' and s[-1] == '6':
        days = [day for day in cal.itermonthdays(year, 1)]
        if days[4] == 1:
            years.append(year)

# Which results in 11 possible matches
print years

# Searching for an important event on January 27th and the above years leads to a solution