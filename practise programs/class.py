class Dog:

    def bark(self):
        print("the dog is barking")

    def add_one(self, x):
        return x + 1


d = Dog()
d.bark()
print(d.add_one(5))
