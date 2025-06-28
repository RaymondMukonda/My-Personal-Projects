#Sets: unordered, mutable, no duplicates
myset = {1, 1, 2, 2, 3} #notice how sets just ignore the duplicates
print(myset)
#another way to create a set
myset2 = set("Hello")
print(myset2) #notice how the words a mixed also every time you print / bec a set is unordered
# how to create an empty set
print("")
myset3 = set()
print(type(myset3))
#add into the set
myset3.add(1)
myset3.add(2)
myset3.add(3)
print(myset3)
print("")
#you can add sets toget using union / union creats two sets without duplication
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8, 10}
primes = {2, 3, 5, 7}
u = odds.union(evens)
print(u)
# you can get inetersection of numbers/ meaning it will print the same numbers that bot sets have 
i = odds.intersection(evens) #nothing will print bec they the same
x = odds.intersection(primes)
print(i)
print(x)
print("")
#this is to check the diffrence of whats missing
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB) #you can place set be where a is to also check where the diffrence is 
print(diff) #will print out the difference 
#this dottom code will check and print what they have in diffrence as in what both have that are diffrent from 
#each other
diff = setA.symmetric_difference(setB)
print(diff)
#you can do this to update you set with seb to get a perfecrt set
set8 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set9 = {1, 2, 3, 10, 11, 12}
set8.update(set9)
print(set8)