# and is just and and or is just or 😃
# Python evaluates not first, then and, then or.
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) #prints true
print('mushrooms' not in requested_toppings) #prints false

b = False
c = False
for a in requested_toppings:
    if a == 'mushrooms':
     b = True
    elif a == 'onions':
     c = True
if (b == True and c == True):
    print("Ooh! Both mushrooms and onions! yum yum!")

# if condition:
#     statement
# elif condition2:
#     statement2
# else:
#     statement3

if requested_toppings: #returns false if list is empty
    pass #just nothing
'''
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
'''
#-----____ elif____-----
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

#short hand if
if a > b: print("a is greater than b") 

#short hand if else
print("A") if a > b else print("B") 


#----------
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 
#all are false

# ------------_____ match_____---------
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")
    case _:
        pass


month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")


#_____ loops

# With the continue statement we can stop the current iteration,
# and continue with the next:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")