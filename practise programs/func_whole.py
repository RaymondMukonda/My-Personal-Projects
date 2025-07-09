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
def foo1(a, b, c, d=4): # default argument # default can only be at the end
    print(a, b, c, d)
foo1(1, 2, 3)
# but you can still change the deault value as so
foo1(1, 2, 3, 7) # the 7 will take the 4s position 
print("")
################################################################################
# *args and **kwargs are special syntaxes that allow functions to accept a variable number of arguments. They provide flexibility when the exact number of arguments a function will receive is unknown at the time of its definition

# The single asterisk * before a parameter name (conventionally args) in a function definition indicates that the function can accept an arbitrary number of non-keyword (positional) arguments.

# one star means you ca pass any number of positional argemnts to your function
# if you mark you parameter with two stars you can pass any number of [ key words] arguments to this function 

def foo2(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo2(1, 2, 3, 4, 5, six=6, seven=7) # mix
# 3, 4, 5 are args and six and seven are kwargs 
print("")
# this is another way to us epositional arguments

def noo(a, b, *, c, d): # evrthng after the star must have a key or it wont work
    print(a, b, c, d)
noo(1, 2, c=3, d=8) # without the keys it wont work 
print("")
# same code above but difrent way
def noo2(*args, last):
    for arg in args:
        print(arg)
    print(last) #PUT OF OF THE LOOP OR IT WILL PRINT AFTER EACH ARG,1 100 2 100
noo2(1, 2, 3, last=100)
print("")

######################## Unpacking Arguments ###################################
def moo(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2]
moo(*my_list)
# we place my list into th function then the * places the list into key argumets so a = 0 , b = 1 etc [ keep in mind the lengeth of your paramiter(list) must match the keys lenght in the function or it will blow up]

# unpack dictionary ############################################################

my_dict = {"a": 1, "b": 2, "c": 3} # key values must match func
moo(**my_dict) # must use two stars
print("")
##################### Local vs Global Variables ################################


number = 0 # global var


def mook():
    global number 
    number = 3 # told otherwise 
    x = number
    print("number inside function", x)



mook() # will always print 0 bec of global number unless told otherwise
print("")
################# Call by object ######################################

def lists(a_list):
    a_list.append(4)

my_list5 = [1, 2, 3]
lists(my_list5)
print(my_list5)