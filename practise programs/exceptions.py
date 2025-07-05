
x = 2

try:
    # print(x/1)
    if not type(x) is str:
        raise TypeError("only strings  are allowed")
except NameError:
    print("NameErros means something is undefined.")
except ZeroDivisionError:
    print("Please do not divide by zero.")
except Exception as error:
    print(error)
else:
    print("No errors!")

finally: #the finally will always print 
    print("I'm going to print with or without an errors.")
 