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
    
#this is calling the the fuction to print on its own without print
d = Dog("tom")
d2 = Dog("molly")
print("")
#this will get what ever name is stored within the assgined d or d2 arguments
print(d.get_name())
print(d2.get_name()) #after printing the output should be the same.
#print out the name stored in just like above 
print(d.name)
print(d2.name)
#pass in the two arguments specified in the dog class otherwise an error will occur
d = Dog("timmy", 34)
print(d.get_age())
#this fuction gets modified by taking the previous func and rebranding it.
d = Dog("tim", 34)
d.set_age(23)
print(d.get_age())


# # more complex class

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age 
        self.grade = grade # 0 - 100 

    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name 
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("rammy", 19, 95)
s2 = Student("tommy", 21, 75)
s3 = Student("johnny", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())
#this will print false and grade ave will remain same
print(course.add_student(s3))
print(course.get_average_grade())
# print(course.students[0].name)


# ####### inheritence###### place the funtion within the class agruments 


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"i ma {self.name} and i am {self.age} years old")

    def speak(self):
        print("i dont know how to speak")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("moew")

    def show(self):
        print(f"i am {self.name} and i am {self.age} years old and im {self.color}" )

class Dog(Pet):
    def speak(self):
        print("barrk")

class Fish(Pet):
    pass

#assign it then call it
p = Pet("timmy", 17)
p.show()
p.speak()
print("")
#the p was assign to pet so in other words the p is a child of pet and will inheret everything thats in the when called 
#p.speak will be diffrent bec the others are using thier own local speak rather then inhereint from the Pet.
#if the inhrent method is the same in the upper level and lower the program will overide and takes whats local meaning whats

# here is another example of how it works will name a funtion but not define it and let it inherent the speak method
f = Fish("jerry", 34)
f.speak()
#the output will be i dont know how to speak


c = Cat("billy", 12)
c.show()
d = Dog("merry", 23)
d.show()
print("")
# if you call whats within the dog and cat funtion youll get :
d.speak()
c.speak()

#super referreces the parent class Pet / super stands for the class we inheri from
c = Cat("molly", 56, "brown")
c.show()
1
2
3