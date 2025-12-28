#notes
# "This is a string."
# 'This is also a string.'
# 'I told my friend, "Python is my favorite language!"'
# "The language 'Python' is named after Monty Python, not the snake."
# "One of Python's strengths is its diverse and supportive community."
# string f:
name = "ada lovelace"
print(name.title())
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
# rstrip() use this to strip a string from spaces at right lstrip() for left spaces

#in python int:
# >>> 3 / 2
# 1.5
# Exponentiaton
#>>> 3 ** 2
# 9
# 

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message) #this is right ^^
# 

#LISTS
# Python has a special syntax for accessing the last element in a list. By ask-
# ing for the item at index -1, Python always returns the last item in the list:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1]) #returns specialized
bicycles.append('ducati') #adds elemnt to the end of the list

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles) #prints: ['ducati', 'honda', 'yamaha', 'suzuki']
del motorcycles[0] #deletes

motorcycles = ['ducati','honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".") #The last motorcycle I owned was a Suzuki.
first_owned = motorcycles.pop(0) #anyposition

motorcycles.remove('ducati') #removing by value
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

