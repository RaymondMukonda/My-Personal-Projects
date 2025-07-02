#Lambda: These functions are small, single-expression functions that can be defined inline without a formal def statement. Lambda functions are often used for short, simple operations where defining a full function would be cumbersome or unnecessar.

# in short lambda allows you to make one line functions

add10 = lambda x: x + 10
print(add10(5))
# the code above is the same as the function below
def add10_func(x):
    return x + 10
print(add10(5)) # print and see same output.
print("")
# another exemple this will take ywo arguments and times them 
mult = lambda x,y: x * y
print(mult(5,5))

# here eis another way
points2d = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2d_sorted = sorted(points2d, key=lambda x: x[1])
# this will sort the list according to the y values ( index 1 )
print(points2d)
print(points2d_sorted)
# that code is the same as 
def sort_by_y(x):
   return x[1] # then call it in the code

points2d_sorted = sorted(points2d, key=sort_by_y)
print(points2d_sorted) # the output should be the same 
