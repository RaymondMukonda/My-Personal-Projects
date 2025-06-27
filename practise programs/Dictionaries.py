#Dictionary: Key-Value pairs, Unordered, Mutable
mydict = { 
  "name": "max",
  "age": 28,
  "city": "Newyork"
 }
print(mydict)
print(type(mydict))
#anotehr way to create dictionaries
mydict2 = dict(name="marry", age=27, city="mozambic")
print(mydict2)
print(type(mydict2))
print("")
#to acess a value use
value = mydict2["name"] #remmeber always use [ ] to call something or fetch it
print(value)

#ths will help you check in the name max is sortered within. dont forget
# name is a (key) and max is a (value) so to check youd need to call it like below
if "max" in mydict.values():
    print("name max is sorted within")
print("")