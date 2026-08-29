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
#.replace("s1","s2") replaces s1 with s2
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 
'''
capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()   	Sets the tab size of the string
find()      	Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isascii()	    Returns True if all characters in the string are ascii characters
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()  	Returns True if all characters in the string are printable
isspace()   	Returns True if all characters in the string are whitespaces
istitle() 	    Returns True if the string follows the rules of a title
isupper()   	Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()    	Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()   	Returns a tuple where the string is parted into three parts
rsplit()    	Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()     	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()    	Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning
'''

#----------------f-string!
'''
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
To specify a string as an f-string, simply put an f in front of the string literal,
and add curly brackets {} as placeholders for variables and other operations.
'''
age = 36
txt = f"My name is John, I am {age}"
print(txt)


'''
A placeholder can contain variables, operations, functions, and modifiers
to format the value.
A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting
type, like .2f which means fixed point number with 2 decimals
price = 56
txt = f"The price is {price:.2f} dollars"
A placeholder can contain Python code, like math operations
'''


#--------excape character
txt = "We are the so-called \"Vikings\" from the north."

"""
\'   	Single Quote 	
\\ 	    Backslash 	
\n   	New Line 	
\r 	    Carriage Return 	
\t   	Tab 	
\b     	Backspace 	
\f 	    Form Feed 	
\ooo 	Octal value 	
\xhh 	Hex value
"""

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


#You have to use the same number of spaces in the same block of code, 
# otherwise Python will give you an error:
# Semicolons!!! (Optional, Rarely Used)
print("Hello"); print("How are you?"); print("Bye bye!") 

x, y, z = "Orange", "Banana", "Cherry"


"""
Text Type:  	str
Numeric Types: 	int,         float,      complex
Sequence Types: list,        tuple,     range
Mapping Type: 	dict
Set Types:  	set,         frozenset
Boolean Type: 	bool
Binary Types: 	bytes,       bytearray,  memoryview
None Type:   	NoneType
---------------------------------------------------
import random

print(random.randrange(1, 10)) 
---------------------------------------------------
Arithmetic operations
+ 	Addition 	    x + y 	
- 	Subtraction 	x - y 	
* 	Multiplication 	x * y 	
/ 	Division 	    x / y 	 always a float answer
% 	Modulus 	    x % y 	
** 	Exponentiation 	x ** y 	
// 	Floor division 	x // y    always integer(rounds down)

assignment 
=      	x = 5 	        x = 5 	
+=  	x += 3 	        x = x + 3 	
-= 	    x -= 3          x = x - 3 	
*=   	x *= 3  	    x = x * 3 	
/= 	    x /= 3          x = x / 3 	
%=  	x %= 3          x = x % 3 	
//= 	x //= 3     	x = x // 3 	
**= 	x **= 3 	    x = x ** 3 	
&=  	x &= 3         	x = x & 3 	
|=  	x |= 3      	x = x | 3 	
^=     	x ^= 3      	x = x ^ 3 	
>>= 	x >>= 3 	    x = x >> 3 	
:= 	    print(x := 3)   x = 3; print(x)

ternary op
num = 6
x = "WEEKEND!" if num > 5 else "Workday"

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

chaining comparison
print(1 < x < 10)
print(1 < x and x < 10)

identity op
Identity operators are used to compare the objects, not if they are equal,
but if they are actually the same object, with the same memory location
is
is not

is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal

membership op
Membership operators are used to test if a sequence is presented in an object
in
not in  

bitwise op
&  	AND 	                x & y 
    Sets each bit to 1 
    if both bits are 1 		
| 	OR 	                    x | y 
    Sets each bit to 1 
    if one of two bits is 1 		
^ 	XOR 	                x ^ y
    Sets each bit to 1 if 
    only one of two bits
    is 1 	 	
~ 	NOT 	                ~x 
    Inverts all the bits 		
<< 	Zero fill left shift 	x << 2
    Shift left by pushing
    zeros in from the right
    and let the leftmost
    bits fall off 	 	
>> 	Signed right shift 	    x >> 2
    Shift right by  	
    pushing copies of the leftmost bit 
    in from the left, and let the rightmost
    bits fall off

precedence order
() 	Parentheses 	
** 	Exponentiation 	
+x  -x  ~x 	Unary plus, unary minus, and bitwise NOT 	
*  /  //  % 	Multiplication, division, floor division, and modulus 	
+  - 	Addition and subtraction 	
<<  >> 	Bitwise left and right shifts 	
& 	Bitwise AND 	
^ 	Bitwise XOR 	
| 	Bitwise OR 	
==  !=  >  >=  <  <=  is  is not  in  not in  	Comparisons, identity, and membership operators 	
not 	Logical NOT 	
and 	AND 	
or 	OR
"""


