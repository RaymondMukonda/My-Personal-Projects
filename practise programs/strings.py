# strings: ordered, immutable, text representation
my_string = "I'm a programmer "
# go over mutiple lines / it will be printed downing down wards
my_string = """Hello

World"""
print(my_string)
# but if you put a slash like this it will then not print in a new line 
my_string1 = """Hello \

World"""
print(my_string1)# this will print out one below the other without the indented space that was given in the ecode
# this is how you can get / fetch fro strings 
print("")
my_string2 = "Hello World"
char = my_string2[1] #you can also get negative numbers -1
print(char)
#how to start one place and end to another
string = "hello people"
substring = string[1:5]
print(substring)
print("")
# concatination adding two or more strings together 
greeting = "Njani"
name = "rammy"
sentence = greeting+ " " + name
print(sentence) 
# this way you can  replace a string 
the_string = "Hello neigbour"
print(the_string.replace("Hello", "stranger")) #this subs out hello and puts 
print("")
# stranger / if the is a typo it will not change
# the old method of calling strings / f strings
name1 = "raymond"
string3 = "hey is your name %s? if so how are you %s !" %(name1, name1) #if you gonna use the same variable place it two or how many times youd like to use it within brakects others if you usinh two diffrent ones you dont have to.
print(string3)
#be careful how you use the % and where you place it for expl
name2 = "mosses"
name3 = "mukonda"
string4 = "hey %s %s how are you doing today? " %(name3, name2)
#this is going to print out hello mukonda mosess intead of mosses mukonda bec of the way we set it in the format
print(string4)
print("")
+#here is another way to formate the string with f string
var = 3.1234567
my_string5 = "the varibale is {:.2f}".format(var)#so you call what you want to formate and python places the value into the open brackets. .2f specifys how many decimal points pyton should go to.
print(my_string5)# see output in terminal
#adding more values as we did with the other code
var = 3.1234567
var2 = 6
my_string6 = "the varibale is {:.2f} and {}".format(var, var2)
print(my_string6)
print("")
