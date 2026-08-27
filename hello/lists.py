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

