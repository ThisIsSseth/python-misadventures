def greets(): #the key word def is used to define a function
    """Prints a simple greeting.""" #docstring: the caption
    print("hi :)")
#the body of the function is detemined by indentation 

greets()

def greeting_user(username): #parameter in the definition 
    print("Hi, " + username.title())

greeting_user("lola") #argument passed to funtion

def describe_pet(animal_type, pet_name): #positional arguments
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#keyword arguments:
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
# both yeild:
#I have a hamster.
# My hamster's name is Harry.

#!: none default parameter shouldn't follow a default one
def describe_pet_default( pet_name, animal_type = "dog"): 
    print("\nI have a " + animal_type + ".")   
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#positional-only
def my_function(name, /):
  print("Hello", name)

my_function("Emil")

#keyword-only
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil") 

#combining both onlys
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result) 

# *args to tuple
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5)) 

# **kwargs for keyword arguments
# Inside the function, kwargs becomes a dictionary containing all the
# keyword arguments:
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen") 
'''
for combos:
    The order must be:

    regular parameters
    *args
    **kwargs
'''

#unpacking *args and ***kwargs
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result) 

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes") 



#returning:
def plus_one(number):
    return number + 1

print(plus_one(5))

#passing a list vs a copy of the list to a function
def inspect_list(list):
    for x in range(0, len(list)):
        print(list[x])
    list.clear()

def inspect_list2(list):
    while(len(list) > 0):
        print(list[0])
        list.pop(0)

        
list = [1, 2, 3]

inspect_list2(list[:])#this one doesn't modify the original, cuz
#the argument is a copy
print(list)
inspect_list2(list)
print(list)

# ----___ closure___------------------------------
def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = create_counter()

print(counter())
print(counter())
print(counter())
# outcome
# 1
# 2
# 3
# The function is carrying state across calls without using a class.


#----___ decorator___-------------------------------
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

# more example
def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))


#----____
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

'''
Functions in Python has metadata that can be accessed using the __name__
and __doc__ attributes

'''


#----____ lambda____-----------------------------
# a smol function
x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) 

#usage example
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#lambda's built in functions
#map
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#sort
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words) 