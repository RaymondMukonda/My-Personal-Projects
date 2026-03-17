# generators are a special type of function or expression that produce a sequence of values on demand, rather than generating and storing the entire sequence in memory at once.

def my_generator():
    yield 1
    yield 2
    yield 3


g = my_generator()
# for i in g :
#     print(i) tis will print eveerything stored individually / code below wont run if this isnt commented out

value = next(g) # this func will run and stop at first yield
print(value) 

value = next(g) # then when run again it will start from 1 and run 2 and stop
print(value)

value = next(g)
print(value)
print("")
# value = next(g)
# print(value) # but once you run it for the forth timre it will break at fourth ( stop itteration)

def countdown(num):
    print("Staring")
    while num > 0:
        yield num
        num -= 1

cd = countdown(4) # this wont run bec of the code
value = next(cd) # it will start but stop bec of cd value 4 
print(next(cd)) # this will make it continue from where it stopped but minus from 4 to 3 then stop again 

# print(cd) # out put should be 3
# run the code till nothing is left
print(next(cd)) # it will rember its last value
print(next(cd))
# print(next(cd)) # this will blow up ( stop iteraton)
print("")

# Genarators are very memory efficient, for when you work with large data
##########################################################################

import sys

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1 
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1 

print(firstn(10))
print(sum(firstn(10))) # will print the total sum together
print(sum(firstn_generator(10))) # this will do the same as above code

# this will show you which takes up more memory
print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))
print("")