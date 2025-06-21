# class Dog:

#     def bark(self):
#         print("the dog is barking")

#     def add_one(self, x):
#         return x + 1

# d = Dog()
# d.bark()
# print(d.add_one(5))

##innit allows you to name the dog funtions 

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print(name)

    #anoher way to print what vaule is givven 02
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    #this allows you to modfie a funtion that has already been set
    def set_age(self, age):
        self.age = age
    
# this is calling the the fuction to print on its own without print
# d = Dog("tom")
# d2 = Dog("molly")
# print("")
# #this will get what ever name is stored within the assgined d or d2 arguments
# print(d.get_name())
# print(d2.get_name()) #after printing the output should be the same.
# #print out the name stored in just like above 
# print(d.name)
# print(d2.name)
#pass in the two arguments specified in the dog class otherwise an error will occur
# d = Dog("timmy", 34)
# print(d.get_age())
#this fuction gets modified by taking the previous func and rebranding it.
# d = Dog("tim", 34)
# d.set_age(23)
# print(d.get_age())
