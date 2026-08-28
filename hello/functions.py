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

def describe_pet_default( pet_name, animal_type = "dog"): #!: none default parameter shouldn't follow a default one
    print("\nI have a " + animal_type + ".")   
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


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
print(list)
inspect_list2(list)
print(list)
#the argument is a copy