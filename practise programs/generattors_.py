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

# value = next(g)
# print(value) # but once you run it for the forth timre it will break at fourth ( stop itteration)

def countdown(num):
    print("Staring")
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)
