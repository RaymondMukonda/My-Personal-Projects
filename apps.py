# # Define our 3 functions
# def my_function():
#     print("Hello From My Function!")

# def my_function_with_args(username, greeting):
#     print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

# def sum_two_numbers(a, b):
#     return a + b

# # print(a simple greeting)
# my_function()

# #prints - "Hello, John Doe, From My Function!, I wish you a great year!"
# my_function_with_args("Raymond Mukonda", "How has your year been!")

# # after this line x will hold the value 3!
# x = print(sum_two_numbers(1,2))

# people_name = input("what is your name? ")

# if people_name == "raymond":
#     (my_function_with_args("Raymond", "Hope you having a good day"))

# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["jonh", "mike", "welcome", "key"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "raymond"

def name_the_benefits_of_functions(username):
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions("smith")