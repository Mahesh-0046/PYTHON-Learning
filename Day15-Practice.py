'''Python modules
Create a module 
Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name)'''

#Use a module
import mymodule
mymodule.greeting("jonathan")

#Variables in a module
import mymodule
a = mymodule.person1["age"]
print(a)

#Built in Modules
import platform
x = platform.system()
print(x)

#Using the dir() Function
import platform
x = dir(platform)
print(x)

#Import from module
from mymodule import person1
print(person1["age"])

#Different ways to import:
#Basic import
import math
print(math.sqrt(16))

#Import with alias
import math as m
print(m.pi)

#Import specific items
from math import sqrt, pi
print(sqrt(25), pi)

#Import Everything
from math import *

#Access module metadata
import math
print(dir(math))
print(math.__doc__)

#Python dates
import datetime
x = datetime.datetime.now()
print(x)

#Date output
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#Creating date objects
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

#the strftime() method
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))