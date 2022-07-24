from collections import Counter

a = 'aaabbbbbcc'
my_counter = Counter(a)
print(my_counter) #dict
print(my_counter.items()) #list of tuples (val,key)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(2)) #2 most common items
print(my_counter.most_common(2)[0][0]) #most common key
print(list(my_counter.elements())) # list ['a','a','a','b','b'...]

from collections import namedtuple

Point = namedtuple('Point', 'x,y')
p1 = Point(1,-1)
print(p1) # Object of Point
print(p1.x)

from collections import OrderedDict

#Remeber order, in 3.7>= version normal dict do it too
dict = OrderedDict()
dict['a'] = 1
dict['b'] = 3
dict['c'] = 2
print(dict)

from collections import defaultdict

dict = defaultdict(int)
dict['a'] = 1
dict['b'] = 2
print(dict['c']) #default value 0

from collections import deque

dq = deque()
dq.append(1)
dq.append(2)
dq.appendleft(3)
print(dq) #[3, 1, 2]

dq.pop() #del 2
print(dq)
dq.popleft() # del 3
print(dq)

dq.extend([2,3,4])
print(dq) #append at the end
dq.extendleft([0, -1])
print(dq) #append left (first appendleft 0 then appendleft -1 so -1 is most left

dq.rotate(1)
print(dq) #all element go 1 step right
dq.rotate(-1)
print(dq) #all element go 1 step left

