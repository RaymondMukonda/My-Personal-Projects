# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "mango", "apple", "orange", "grape" ]
print(mylist)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)
print("")

# get an index / banana = 0 / mango = 1 / apple = 2
item = mylist[0]
print(item)
print("")
# you can get the last item with negavtive -1 / whiich will be grape
item = mylist[-1]
print(item)
print("")
# to interate throught them you can do this(pritn them line by line)
for i in mylist:
    print(i)

#  to check if anitem is in the list
if "banana" in mylist:
    print("banana is in the list")
# else: if banan is not in the list this code will run
#     print("banana is not in the list")
print("")

# print how many items in in a list
print(len(mylist))

# to add items into the list you use bracts 
mylist.append("lemon")
print(mylist)
# if you want to place an item at a specific place /  index(we use the inssert method)
# add the indx first then thr item
mylist.insert(1, "blueberry")
print(mylist)
print("")
# the pop item removes the last item
items = mylist.pop()
print(items)
print(mylist) #youll  see tht lemon is out the list

# you can also remove a specific element
items = mylist.remove("blueberry")
print(mylist) #youll see that blueberry goes out the list
print("")
# this removes evry thng from the list
# items = mylist.clear()  comment in out so that thr list isnt emepty
# print(mylist)
items = mylist.reverse()
print(mylist)

# this will sort your numbers alferbeti
items = mylist.sort()
print(mylist)
print("")

# to print the same thing in a list a number of times
newlist = [0] * 5
print(newlist) 
# to add to list together you can
newlist2 = [1, 2, 3, 4, 5]
newwest = newlist + newlist2
print(newwest)
print("")

#to get a specofic range of numbers:
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
splist = list1[1:5] # index see is 5 but this fuction means = to but not including 5, meaning to index 6 as 5 youd need to add till 6
print(splist)