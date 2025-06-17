f = open("names.txt")
# print(f.read())
# print("")
# print(f.readline())
# print(f.readline())
for line  in f:
    print(line)

f.close()

try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("The file you are trying to open doesnt not exist.")
finally:
    f.close()

# append - creates a file if it doesnts exist

f = open("names.txt", "a")
f.write("\nNdeka")
f.close()

f = open("names.txt")
print(f.read())
f.close()

###write (overwrite) creates a new file
f = open("context.txt", "w")
f.write("I deleted all context")
f.close()


f = open("context.txt")
print(f.read())
f.close()

