def greetUser():
    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")
    age = input("Please enter your age: ")
    return name, surname, age   # return values

def getUserData():
    name, surname, age = greetUser()  # unpack returned values
    print(f"Hello {name} {surname}, we are aware that you are {age} years old")