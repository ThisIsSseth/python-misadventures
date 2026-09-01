#----_____tuples _____---------------------------
# Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
dimensions = (200, 50)
# Tuples can also be created without the parentheses
dimensions = 200, 50
# dimensions[0] = 250 -> ERROR: TypeError: 'tuple' object does not support item assignment
# what we can do:
dimensions = (400, 100)
# also Once a tuple is created, you cannot change its values. Tuples are
# unchangeable, or immutable as it also is called. But there is a
# workaround. You can convert the tuple into a list, change the list,
# and convert the list back into a tuple. using list() and tuple()
'''
no .append() support but we can do both above and:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
'''

# unpacking when the numbers don't match is by *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

# tuple with one item
thistuple = ("apple",)

#NOT a tuple
thistuple = ("apple")
# empty tuple 
thistuple = ()

#multiplying a tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

for dimension in dimensions:
    print(dimension) #returns all the elements in the tuple like in a list
#400
#100

# .count()	Returns the number of times a specified value occurs in a tuple
# .index()


#----____dictionary ____-------------------------
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) #dictionaries are dynamic memories

del alien_0['points']
#to delete a key value

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
          language.title())


# other types of loops:
# for name in favorite_languages:
# for name in favorite_languages.keys(): .keys() returns a list

for language in set(favorite_languages.values()):
    print(language.title())
    # When you wrap set() around a list that contains duplicate items, Python
#   identifies the unique items in the list and builds a set from those items.

# nesting: to store a set of dictionaries in a list or a list of items 
# as a value in a dictionary.

# The items() method will return each item in a dictionary, as tuples in a list.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020}) 

for x in thisdict.keys():
  print(x) 

for x in thisdict:
  print(x) 
  #keys


for x in thisdict.values():
  print(x) 

for x in thisdict:
  print(thisdict[x]) 
  #values

for x, y in thisdict.items():
  print(x, y) 

'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''

