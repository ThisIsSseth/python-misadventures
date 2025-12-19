#syntax
if 5>2:
    print("5 is greater than 2!")
###python uses indentation to indicate a block of code.
#*Also comments are made with #### <- these
# !!!
# LOL #

# if 5 > 2:
# print("Five is greater than two!") //ERROR!

###The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
if 5 > 2:
 print("Five is greater than two!")  #OK
if 5 > 2:
        print("Five is greater than two!") #OK

#if 5 > 2:
# print("Five is greater than two!")
#        print("Five is greater than two!") //Also ERROR!!!

print("Hello World!", end=" ")
print("I will print on the same line.")

# About declacring TYPEs:
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Casting:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y)) 

#take note that
#  Variable names are case-sensitive.

# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"

#If you have a collection of values in a list, tuple etc. Python allows you to
# extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

x = "Python"
y = "is"
z = "awesome"
print(x, y ,z) #this one adds spaces on its own
print(x + y + z) #this one doesn't

