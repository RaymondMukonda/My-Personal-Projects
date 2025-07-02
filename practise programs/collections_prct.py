#Collections: Counter, namedtuple, OrderdDict, defaultdict, Deque
#Counter/ stores elemnts as dictionary keys and ther counts as dictionary values
from collections import Counter
a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter) #see out put in terminal
print(my_counter.most_common(1))#this will print out the most common between them all
print(my_counter.most_common(1) [0] [0]) #by adding one 0 this will get you the elemnt and avalue, by adding another 0 this will only  get you the value which is a

from collections import namedtuple

Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt) # this will print everything together you can fect the two var individually
print(pt.x, pt.y) #see diffrence in output
print(type(pt))


from collections import OrderedDict
# this is the same as an ordinerey dict only diffrenece is this one rembers 
# the order the item was inserted. but ts now nuneccry bec new pthon dict can do them same 
