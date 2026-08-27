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
#.clear() empties the list

#len(thislist) get the size of the list

