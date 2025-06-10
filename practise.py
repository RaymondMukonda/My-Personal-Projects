# def sum(num1,num2):
#     return num1 + num2

# total = sum(2, 3)
# print(total)

# def multiple_items(*args):
#     print(args)
#     print(type(args))

# multiple_items("dave", "john", "sara")


# def mult_named_items(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# mult_named_items(first = "Dave", last = "Gray")

# value = "y"
# count = 0

# while value:
#     count += 1
#     print(count)
#     if (count == 5):
#         break
#     else:
#         value = 0 
#         continue

# name = "dave"
# count = 2

# def greeting():
#     color = "blue"
#     global count 
#     count += 1
#     print(count)

#     def another(name):
#         nonlocal color
#         color = "red"
#         print(color)
#         print(name)

#     another("rammy")


# greeting()


# def parent_function(person, coins):
#     # coins = 3

#     def play_game():
#         nonlocal coins
#         coins -= 1

#         if coins > 1:
#             print(f"\n{person} has {coins} coins left")
#         elif coins == 1:
#             print("\n" + person + " has " + str(coins) + " coin left.")
#         else:
#             print("\n" + person + " Is out of coins.")
            

#     return play_game

# Rammy = parent_function("Rammy", 3)
# susan = parent_function("susan", 5)

# Rammy()
# Rammy()
# susan()
# Rammy()

person = "rammy"
coins = 3

mail = "\n%s has %s coins left." %(person,coins)
text = "\n%s has %s coins left." %(person,coins)
message = "\n{1} has {0} coins left." .format(coins, person)
print(message)
print(text)
print(mail)

