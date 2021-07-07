#List slices
'''It provide a more advanced way of retrieving values from a list. 
Basic list slicing involves indexing a list with two colon-separated integers.
This returns a new list containing all the value in the old list between the
indices.'''
squares=[0,1,4,9,16,25,36,49,64,81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
'''like the arguments to range, the first index provided in a slice is included 
in the result, but the second isn't.'''
#to reverse the whole list use[::-1]
print(squares[::-1])

#if the first number in a slice is omitted, it's taken to be the start of the list
#if the second number in a slice is omitted, it's taken to be the end
#if the 2nd. is bigger than last key, still grt the same result
print(squares[:7])
print(squares[7:])
print(squares[7:100])
print(squares[:]) #print whole list
#print(squares[]) #SyntaxError: invalid syntax
print(squares[7:-1])
print(squares[7:-0])
print(squares[2:-3])
print(squares[2:-8]) #the seconsd cross 1st will returm  []
print(squares[2:-0]) #the 2nd be -0 will returm  []
#slicing can also be done on tuples.
print(squares[::-2]) #revese result with every2
print(squares[2:8:3])#incluse element starting from the 2nd indexup to the 8th with a step of 3
print(squares[::1])
print(squares[::2])
print(squares[0::4])

#the index count will always be from the beginning.
#Note that we can go in the reverse direction because the step is negtive.
print(squares[7:6:-1])   #[49]
print(squares[7:5:-1])  #[49, 36]
print(squares[7:2:-2])  #[49, 25, 9]
print(squares[7:2:1])  #[]
