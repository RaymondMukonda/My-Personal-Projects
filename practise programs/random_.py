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