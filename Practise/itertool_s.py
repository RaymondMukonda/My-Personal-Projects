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
print("")


from itertools import combinations,  combinations_with_replacement
# will make all possible combinations possibe /
# rember you cant  have combinations of the same argument[ 1, 2, 3, ]
# if you want that then you'd have to do this add , combinations_with_replacement
g = [1, 2, 3, 4]
comb = combinations(g, 2) # to see all numbers dont add a specification just (g)
print(list(comb))
comb_wr = combinations_with_replacement(g, 2)
print(list(comb_wr)) # see diffrence in the terminal
print("")

from itertools import accumulate
import operator
# it will add left to right 1 + 2 = 3 +  3 = 6 + 4 = 10
h = [1, 2, 3, 4]
acc = accumulate(h)
print(h)
print(list(acc)) # see output on terminal
# you can also multiply by adding aperator
acc2 = accumulate(h, func=operator.mul)
print("")
print(h)
print(list(acc2)) # 1 times 1 = 1 times 2 = 2 etc
print("")

from itertools import groupby

def smaller_than_3(x):
    return x < 3

i = [1, 2, 3, 4]
group_obj = groupby(i, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value)) # the output will be grouped on what is true and what is false. this mthod helps us group catagoriess that are of the same.


from itertools import count, cycle, repeat # infinite iterators

for i in count(10): # this will start at ten
    print(i)
    if i == 15: # this will make it stop at 15 / if not told it will run forever
        break

o = [1, 2, 3] # thhis will print 1 2 n 3 coninoiusly until told not to
for i in cycle(o):
    print(i)
    if i == 3:
        break

print("")
for i in repeat(1, 4):#placing a 4 there means it should only print 1 four times
    print(i)
