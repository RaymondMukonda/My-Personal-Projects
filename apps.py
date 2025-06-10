def sum(num1,num2):
    return num1 + num2

total = sum(2, 3)
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("dave", "john", "sara")


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Dave", last = "Gray")

value = "y"
count = 0

while value:
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = 0 
        continue