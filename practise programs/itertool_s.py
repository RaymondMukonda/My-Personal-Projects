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
print("")

from itertools import permutations
# with this you get to see every outcome of that code that can be written
f = [1, 2, 3]
perm = permutations(f)
print(list(perm))
# you can specify the paramiters as so
perm = permutations(f, 2)
print(list(perm)) # this will limit it to two