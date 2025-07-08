
def start_end_decorator(func):

    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper



def print_name():
    print("alex")

print_name = start_end_decorator(print_name)

print_name()
# so this function  above without the decorator will place the objact print name into it bec end decorator takes a function in its arguments. the code below will show how to use the decorator , it will do the same thing as this line ( print_name = start_end_decorator(print_name) )
print("")

def start_end_decorator(func):

    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper


@start_end_decorator #this @ places the obj inside as tht line did
def print_name():
    print("alex")

print_name()
print("")

# if you objact that you store wintin the otherr doesnt take arguments youll have to do this / the code below wont work bec it takes no arguments

# def start_end_decorator(func):

#     def wrapper(): the wrapper doesnttake any arguments and ous does 
#         print("start")
#         func() and the func doesnt take any arguments
#         print("end")
#     return wrapper

# to fx this do this 


def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper


@start_end_decorator
def add_5(x):
    return x + 5

result = add_5(10)
print(result)

#################################################################
# sum up of decorator function

def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print("start")  # you can do somehting before the function 
        result = func(*args, **kwargs) # then is will run the fuction
        print("end") # then it will do something after the fuction
        return result
    return wrapper

#######################################################################
#  decorator can take a function witin it also 
print("")
import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3) # place how many times you want it to display or exsicute
def greet(name):
    print(f"Hello {name}")

greet("Rammy")
print("")
# this code is how you use decoratetors with arguments seen above 

# you can also next decorators on how you place them on tom of each other aas seen below

def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ",".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})") #prnt info abut name func
        result = func(*args, **kwargs) # exercute
        print(f"{func.__name__!r} returened {result!r}") #prnt info bout return
        return result
    return wrapper


# will be exercuted in order placed (listed)

@debug # 1  # 2 will be calling inside of debug # 6 will print wrapper return
@start_end_decorator # 3 # 5 will will print the end 
def say_hello(name): # 4
    greeting = f"hello {name}"
    print(greeting)
    return greeting

say_hello("Rammy")

# this code above helps to show you what runs first and calls the name so you siee what gets done before what 

##############################################################################
# You ca also use this with classes
print("")
class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0 


    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is exercuted {self.num_calls} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_name_counts():
    print("Hello")

say_name_counts() # every time you call the func it will tell you # 1
say_name_counts() # see out put below # 2