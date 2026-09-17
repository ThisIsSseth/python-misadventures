class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age) 

#that to this:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# you can set default value like  __init__(..., age=18)
# It does not have to be named self, you can call it whatever you 
# like, but it has to be the first parameter of any method in the class

# -----_____ magic methods____----------------------
'''
or dunder methods:
__init__()	Person(...)	Runs when a new object is created
__str__()	print(obj), str(obj)	Controls the readable text shown for an object
__repr__()	repr(obj)	Controls the developer-facing representation
__eq__()	obj1 == obj2	Controls what "equal" means for the class
__add__()	obj1 + obj2	Controls what the + operator does
__len__()	len(obj)	Returns the "length" of an object
__lt__()	obj1 < obj2	Controls how objects are ordered when compared or sorted
__contains__()	item in obj	Controls what the in operator checks
__call__()	obj(...)	Lets an object be called like a function
'''
class ClickCounter:
  def __init__(self):
    self.clicks = 0

  def __call__(self):
    self.clicks += 1
    return self.clicks

button_clicks = ClickCounter()

print(button_clicks())
print(button_clicks())
print(button_clicks())
# Unlike a regular function, it remembers its own state between calls,
# so the count keeps going up each time it is called.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person): #this is how to inherit Person
  def __init__(self, fname, lname):
    super().__init__(fname, lname) 
    # By using the super() function, you do not have to use the name of
    # the parent element, it will automatically inherit the methods and 
    # properties from its parent.
