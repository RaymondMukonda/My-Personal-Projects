def funcBuilder(x):
    return lambda num: num + x

addten = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addten(7))
print(addTwenty(7))


##################################



numbers = [3,7,12,18,20,21]

squared_nums = map(lambda num : num * num, numbers)
print(list(squared_nums))

###################################



odd_nums = filter(lambda num : num % 2 != 0, numbers)
print(list(odd_nums))