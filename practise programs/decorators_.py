
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

