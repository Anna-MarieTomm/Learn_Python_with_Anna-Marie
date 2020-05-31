"""
Docstring: retrieves the current time from the laptop, with the help of the datetime module
"""

#import the datetime module

import datetime


time = datetime.datetime.now().time()
if __name__ == "__main": 
    print (time)
else: 
    print ("please ask your console about the name!")
