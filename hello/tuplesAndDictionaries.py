#----tuples ---
# Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
dimensions = (200, 50)
# dimensions[0] = 250 -> ERROR: TypeError: 'tuple' object does not support item assignment
# what we can do:
dimensions = (400, 100)

for dimension in dimensions:
    print(dimension) #returns all the elements in the tuple like in a list
#400
#100


#----dictionary ---
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
