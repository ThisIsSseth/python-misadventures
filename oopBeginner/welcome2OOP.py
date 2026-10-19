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
__init__()\tPerson(...)\tRuns when a new object is created
__str__()\tprint(obj), str(obj)\tControls the readable text shown for an object
__repr__()\trepr(obj)\tControls the developer-facing representation
__eq__()\tobj1 == obj2\tControls what "equal" means for the class
__add__()\tobj1 + obj2\tControls what the + operator does
__len__()\tlen(obj)\tReturns the "length" of an object
__lt__()\tobj1 < obj2\tControls how objects are ordered when compared or sorted
__contains__()\titem in obj\tControls what the in operator checks
__call__()\tobj(...)\tLets an object be called like a function
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

# -----_____ properties and type hints _____----------------------
# A return type hint such as -> bool documents the type a function or
# method is expected to return. Python does not enforce this at runtime,
# but editors and static type checkers can use it to catch mistakes.
# In this example, -> bool tells readers and tools that is_pending should
# return True or False:
#
# @property
# def is_pending(self) -> bool:
#     return self.giver_operator is None and self.real_return_date is None
#
# @property turns a method into a managed attribute: access it as
# object.is_pending rather than object.is_pending(). The method still runs
# when accessed, so the value is computed from the object's current state.
# Here it returns True only when both giver_operator and real_return_date
# are None. This avoids storing a separate flag that could become stale.
#
# The example assumes giver_operator and real_return_date are attributes
# defined elsewhere in the class. The method returns a bool, but the
# annotation itself does not force that return type.

class LibraryItem:
  def __init__(self, giver_operator=None, real_return_date=None):
    self.giver_operator = giver_operator
    self.real_return_date = real_return_date

  @property
  def is_pending(self) -> bool:
    return self.giver_operator is None and self.real_return_date is None

# Example: item.is_pending (no parentheses) evaluates the property.
# print(LibraryItem().is_pending)  # True

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
