import os 


r = Read
a = Apeeend
w = Write
x = Create

f = open("names.txt")
# print(f.read())
# print("")
# print(f.readline())
# print(f.readline())
for line  in f:
    print(line)

# f.close()

# try:
#     f = open("name_list.txt")
#     print(f.read())
# except:
#     print("The file you are trying to open doesnt not exist.")
# finally:
#     f.close()

# append - creates a file if it doesnts exist

# f = open("names.txt", "a")
# f.write("\nNdeka")
# f.close()

# f = open("names.txt")
# print(f.read())
# f.close()

# ###write (overwrite) creates a new file
# f = open("context.txt", "w")
# f.write("I deleted all context")
# f.close()


# f = open("context.txt")
# print(f.read())
# f.close()

# # two ways to create a new file
# #opens a file for writing, creates the file if it does not exist

# f = open("name_list.txt," "w")
# f.close()

# # creats the specified file, but returns an error if the file exists (will need to create an os)
# if not os.path.exists("dave.txt"):
#     f = open("dave.txt" "x")
#     f.close()

# delete a file
# # aviod a  error if it doesnt exists 
# if os.path.exists("dave.txt"):
#     os.remove("dave.txt")
# else:
#     print("the file you wish to delete")