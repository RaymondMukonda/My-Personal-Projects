# def greet(first_name, surname):
#     print(f"hello there {first_name} {surname}")
#     print("welcome abroad")

# greet("raymond", "mukonda")


## its args and be placed where you see fit
# def greet(name, age):
#     print(f"hello {name} im awere that you are {age} of age right?")
# greet("raymond", 21)


#args allows a function to acccept any number of positional arguments, these arguments are accedd as tuples inside the 
# def greet(*args):
#     for name in args:
#         print(f"hello {name}")
# greet("rammy", "neo", "marry")


# #always name you fuction args as what youd like to place there
# def math_method():
#     value_str = input("give me a number youd like to times: ")
#     value = int(value_str)
#     num_str = input("give me another number you would like to times: ")
#     num = int(num_str)
#     sum_reslut = num * value 
#     print(sum_reslut)
# math_method()