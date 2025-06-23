def greet(first_name, surname):
    print(f"hello there {first_name} {surname}")
    print("welcome abroad")

greet("raymond", "mukonda")


# its args and be placed where you see fit
def greet(name, age):
    print(f"hello {name} im awere that you are {age} of age right?")
greet("raymond", 21)


# args allows a function to acccept any number of positional arguments, these arguments are accedd as tuples inside the 
def greet(*args):
    for name in args:
        print(f"hello {name}")
greet("rammy", "neo", "marry")


# always name you fuction args as what youd like to place there
def math_method():
    value_str = input("give me a number youd like to times: ")
    value = int(value_str)
    num_str = input("give me another number you would like to times: ")
    num = int(num_str)
    sum_reslut = num * value 
    print(sum_reslut)
math_method()

# or you can do it ths way 
def increment(number,by):
    return number + by
print(increment(number=2, by=3))


# 1- perfrom a task / locked to printing somehing in  a terminal
def greet(name):
    print(f"hi {name}")
greet("rammy")


# 2- return a value / reusable 

def get_greeting(name):
    return f"hi {name}"

message = get_greeting("rammy") #can place it into varables
file = open("context.txt", "w") #open a file for writting and will place the name name rammy inside
file.write(message)

# this chances to what you define it to be instead of taking the global value
message = "a"

def greet(name):
    global message
    message = f"hello {name}"
    print(message)

greet("mosh")