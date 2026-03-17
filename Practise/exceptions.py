
x = 2  #change this to strng to see output 

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
print("")


## anotehr example 
try:
    a = 5 / 0
    b = a + 4 
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("everything is fine")
finally:
    print("cleaning up....")

print("")
 

# how you can define your own exception errors 
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message 
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("This value is to high")
    if x < 5:
        raise ValueTooSmallError("Value is to samll", x)
    
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)