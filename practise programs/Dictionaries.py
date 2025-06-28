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
if "max" in mydict.values(): # this soecifically only gets max but you can get all values by doing this 
    print("name max is sorted within")
print("")
#this print out all the values
for value in mydict.values(): #you can place the word key where value is to get the values.
    print(value)
print("")
# or you can print both the key and values at thre same time
for key, value in mydict.items():
    print(key, value)
print("")
#OR YOU CAN do it this way
if "name" in mydict:
    print(mydict["name"]) #it should print out max
#  incase someone places a wrong key you can promt them to do this 
try:
    print(mydict["lastname"])
except:
    print("That value does not exist in my dict")

#this is how you can copy a dictionary otherwise youll end up chaing both
print("")
diction = {"name": "bobby", "age": "34"}
diction_cpy = diction 
diction_cpy["email"] = "booy@yb.com"
print(diction_cpy)
print(diction)
print("")
#once yove done this youll realize that it changes both dictionaries to fic that use the .copy() method
diction1 = {"name": "bobby", "age": "34"}
diction1_cpy = diction1.copy()
diction1_cpy["email"] = "booy@yb.com"
print(diction1_cpy)
print(diction1)
#see the difference