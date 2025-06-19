class Dog:

    def bark(self):
        print("the dog is barking")

    def add_one(self, x):
        return x + 1

d = Dog()
d.bark()
print(d.add_one(5))

##innit allows you to name the dog funtions 

class Dog:

    def __init__(self, name):
        self.name = name
        print(name)

    #anoher way to print what vaule is givven 02
    def get_name(self):
        return self.name
# this is calling the the fuction to print on its own without print
d = Dog("tom")
d2 = Dog("molly")
print("")
#this will get what ever name is stored within the assgined d or d2 arguments
print(d.get_name())
print(d2.get_name()) #after printing the output should be the same.
