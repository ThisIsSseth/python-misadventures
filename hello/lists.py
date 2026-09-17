#LISTS
# Python has a special syntax for accessing the last element in a list. By 
# asking for the item at index -1, Python always returns the last item in the list:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1]) #returns specialized
bicycles.append('ducati') #adds elemnt to the end of the list

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles) #prints: ['ducati', 'honda', 'yamaha', 'suzuki']
del motorcycles[0] #deletes

motorcycles = ['ducati','honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".") 
#The last motorcycle I owned was a Suzuki.
motorcycles.remove('ducati') #removing by value

first_owned = motorcycles.pop(0) #anyposition
# list.sort() -> irrevetible
# or .sort(reverse=True) 
# sorted(list) -> sorts temporarily
# list.reverse() -> to reverse the original order
# len(list) lenght of the list

for value in range(1,5):
 print(value)
#res:
# 1
# 2
# 3
# 4
numbers = list(range(1,6))
even_numbers = list(range(2,11,2))
print (even_numbers)

squares = []
for value in range(1,11):
 square = value**2
 squares.append(square)
print(squares)

squares = []
for value in range(1,11):
 squares.append(value**2)
print(squares)
#another way to do the same thing

squares = [value**2 for value in range(1,11)]
#also another way to do it

#some functions:
print(max(squares))
print(min(squares))
print(sum(squares))

# res:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print (squares[0:3])
# prints elements from 0 to 2 this actually generates a subset of the list
# [:n] from start til the nth 
# [n:] from nth til the end
# [-n:] the last n ones

copy_of_squares = squares[:]
# copy_of_squares = squares -> ERROR
# list2 = list1: list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2.
# mylist = list(thislist) this also does the copying


# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# you can also 
thislist[1:2] = ["blackcurrant", "watermelon"]
# Note: The length of the list will change when the number
#of items inserted does not match the number of items replaced.
thislist.append("orange") #is to the end
thislist.insert(1, "orange") #at specified index
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #adds tropical to end of thislist, it can extend(tuple/set/dictionaries)
#.remove(item)
#.pop()
#.pop(index)
#del
# del thislist #deletes the list completely
#.clear() empties the list
#.reverse
#.sort() method is case sensitive
#.sort(reverse = True)
#len(thislist) get the size of the list

# The range object is a data type that represents an immutable
# sequence of numbers, and it is not directly displayable. 
# Therefore, ranges are often converted to lists for display.
print(list(range(5, 20, 3))) 

#___ unpacking:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

#___ comprehension____
[print(x) for x in thislist] #[] are a must

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
newlist = [x for x in fruits if "a" in x]
print(newlist)

# newlist = [expression for item in iterable if condition == True]
# newlist = [x if x != "banana" else "orange" for x in fruits] 
# "Return the item if it is not banana, if it is banana return orange"



def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)