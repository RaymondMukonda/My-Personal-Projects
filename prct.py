def funcBuilder(x):
    return lambda num: num + x

addten = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addten(7))
print(addTwenty(7))


##################################

