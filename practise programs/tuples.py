#Tuple: oredered, immutable, allows duplicate elements
#tuples are created with parenthasis and separeted by a comma
mytuple = {"max", 26, "south africa"}
print(mytuple)
print("")
# you can still create tuples without parenthesis
mytuple = "max", 26, "south africa"
print(type(mytuple))
print(mytuple)
#to see or get index of something 
print(mytuple.index("max"))
print("")
#you can convert a tuple into a list
my_tuple = "a", "b", "c", "d", "e"
my_tuple = list(my_tuple) #by adding the word list you turn this diction into a list
print(my_tuple)
print(type(my_tuple))
#to turn it back into a tuple use
my_tuple2 = tuple(my_tuple)
print(type(my_tuple2))
print(my_tuple2)
print("")