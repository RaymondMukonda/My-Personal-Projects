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
print("")

from collections import OrderedDict
# this is the same as an ordinerey dict only diffrenece is this one rembers 
# the order the item was inserted. but ts now nuneccry bec new pthon dict can do them same 

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['e'] = 4
ordered_dict['f'] = 5
print(ordered_dict)
print("")

from collections import defaultdict
d = defaultdict(int) #you can place a float, list etc
d["a"] = 1
d["b"] = 2
print(d["a"])
print(d["c"]) #this will bring back the defualt interger we placed at the top if the key we looking for doesnt exist.
print("")

from collections import deque
# its a double ended que that removes characters from both ends / front and
# 3 back

