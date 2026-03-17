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
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3) # will add elements to the left side
print(d)
# usaully when we use pop it removes from the right/ end part
# with this will be able to remove on the left side / start side
d.popleft() # this will remove the 3 
d.pop() # this will remove at the end / right
print(d) # this will print 1 because we removd from both ends 
# add elemnts to the right side 
d.extend([2, 3, 4, 5]) # you can also do this on the left with .extendleft
print(d)
# you can als rotate nubers to the right or left 
d.rotate(1) # this will rotate numbers 1 place to the right meaning to make 1 go all the way to where 5 is you,d put vaule 5 in the bracket
print(d)
# this is how to rotate the other way round
d.rotate(-2)
print(d) # you,'ll see that 1 goes all the way to the back bec of the 2