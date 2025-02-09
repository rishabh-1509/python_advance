#collection module : Counter, namedTuple,OrderedDict,Defualtdict,deque
from collections import Counter
a= '111111111112222222222444444444444433333333333334444444'
my_counter = Counter(a)
print(my_counter)#give the key value pair containg the diffrent element as key and their count as the value
print(my_counter.most_common(1)[0])#gives me the most common element from the list 
print(my_counter.elements())#gives us the intreable element from the list

from collections import namedtuple
 # namedtuple is a built-in Python class that creates a new tuple subclass with named fields
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
print(p.x, p.y)

