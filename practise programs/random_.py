#the numbers seem random but are reproducable
import random

#this will print a roandom number from 0-1
a = random.random()
print(a) # evrtime you print it will give you different number

# you can give it a specific range to choose  from floats
b = random.uniform(1, 11)
print(b)
# if you want a fixed nummber you can 
c = random.randint(1, 11)
print(c)

# this will never pick the upper number(last which is 10)
d = random.randrange(1, 10)
print(d)
print("")

mylist = list("ABCDEFGH")
e = random.choice(mylist) #choice lets it pick from whatever you give it
print(e)

# this code will not pick the same key twice 
e = random.sample(mylist, 3)# well add for it to pick 3 keys so you see
print(e)
# but lets say you want to pick the same item more then once at the same time
e = random.choices(mylist, k = 3)
print(e) # you see it picks the same key twice

#this will shuffle the list
random.shuffle(mylist)
print(mylist)

###############################################################################

