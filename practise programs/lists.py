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