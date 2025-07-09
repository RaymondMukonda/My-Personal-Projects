"""

- The difference between arguments and parameters 
- Positional and Keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Local vs. global arguments
- Prameter passing (by value or by reference?)

"""

# parameters are placeholders defined in a function's declaration, while arguments are the actual values passed to the function when it's called.

def print_name(name): # this name is our parameter 
    print(name)
print_name("Rammy") # tis is the argument for this function

# you can use key word arguments to call stuff
def foo(a, b, c):
    print(a, b, c)

foo(c=1, b=2, a=3) # keys are abc , the order in which you place you keys and values will be diffrent , as you can see ive put c as 1 meaning 3 will be first 
# you also cant assign two keys to one value as in a=1 and a=2

## This is with default arguments d=4 ##
def foo1(a, b, c, d=4): # default argument
    print(a, b, c, d)
foo1(1, 2, 3)
# but you can still change the deault value as so
foo1(1, 2, 3, 7) # the 7 will take the 4s position