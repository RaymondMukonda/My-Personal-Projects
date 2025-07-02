from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a,b)
print(list(prod)) # add the word list for it to print out
# this will join the two numbers on top with the bottom once 

# you can make the list repeat like this 
c = [1, 2]
d = [3]
prod2 = product(c,d, repeat=2)
print(list(prod2)) # see out put in terminal