# Technically, in Python, an iterator is an object which implements the
# iterator protocol, which consist of the methods __iter__() and __next__().

#  Lists, tuples, dictionaries, and sets are all iterable objects. They
# are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# The for loop actually creates an iterator object and executes the
# next() method for each loop.

#To create an object/class as an iterator you have to implement the
# methods __iter__() and __next__() to your object.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# The example above would continue forever if you had enough next()
# statements, or if it was used in a for loop.
# To prevent the iteration from going on forever, we can use the 
# StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise
# an error if the iteration is done a specified number of times:

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


# -----____ modules_____-------------------------

# A file containing a set of functions you want to include in your
# application. -> file extension .py
# we use it by importing it 

# in mymodule.py:
# def greeting(name):
#   print("Hello, " + name) 
# then:
# import mymodule
# mymodule.greeting("Jonathan")

# in mymodule.py:
# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# } 
# then:
# import mymodule
# a = mymodule.person1["age"]
# print(a) 

# ----Create an alias for mymodule called mx:
# import mymodule as mx
# a = mx.person1["age"]
# print(a) 

# There is a built-in function to list all the function names 
# (or variable names) in a module. The dir() function:

#  from mymodule import person1
# When importing using the from keyword, do not use the module name
# when referring to elements in the module. Example: person1["age"],
#  not mymodule.person1["age"]


#-----_____ date and time
import datetime

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A")) 
'''
%a 	Weekday, short version 	Wed 	
%A 	Weekday, full version 	Wednesday 	
%w 	Weekday as a number 0-6, 0 is Sunday 	3 	
%d 	Day of month 01-31 	31 	
%b 	Month name, short version 	Dec 	
%B 	Month name, full version 	December 	
%m 	Month as a number 01-12 	12 	
%y 	Year, short version, without century 	18 	
%Y 	Year, full version 	2018 	
%H 	Hour 00-23 	17 	
%I 	Hour 00-12 	05 	
%p 	AM/PM 	PM 	
%M 	Minute 00-59 	41 	
%S 	Second 00-59 	08 	
%f 	Microsecond 000000-999999 	548513 	
%z 	UTC offset 	+0100 	
%Z 	Timezone 	CST 	
%j 	Day number of year 001-366 	365 	
%U 	Week number of year, Sunday as the first day of week, 00-53 	52 	
%W 	Week number of year, Monday as the first day of week, 00-53 	52 	
%c 	Local version of date and time 	Mon Dec 31 17:41:00 2018 	
%C 	Century 	20 	
%x 	Local version of date 	12/31/18 	
%X 	Local version of time 	17:41:00 	
%% 	A % character 	% 	
%G 	ISO 8601 year 	2018 	
%u 	ISO 8601 weekday (1-7) 	1 	
%V 	ISO 8601 weeknumber (01-53) 	01
'''

x = datetime.datetime(2020, 5, 17)
print(x) 
# The datetime() class also takes parameters for time and 
# timezone(hour, minute, second, microsecond, tzone), but they are 
# optional, and has a default value of 0, (None for timezone).

#-----____ json____------------------------------
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

#-----------------------
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"]) 

'''
You can convert Python objects of the following types, into JSON strings:
    dict
    list
    tuple
    string
    int
    float
    True
    False
    None

When you convert from Python to JSON, Python objects are converted
into the JSON (JavaScript) equivalent:
Python 	JSON
dict 	Object
list 	Array
tuple 	Array
str 	String
int 	Number
float 	Number
True 	true
False 	false
None 	null
'''

json.dumps(x, indent=4)
json.dumps(x, indent=4, separators=(". ", " = "))
json.dumps(x, indent=4, sort_keys=True)

# -----_____ exceptions _____-----------------------

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") 
finally:
  print("The 'try except' is finished") 


try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file") 
