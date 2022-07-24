from itertools import product

a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod)) #list of tupels of all pairs (ai,bi)
b = [0]
prod = product(a,b, repeat = 2)
print(list(prod)) # [(1, 0, 1, 0), (1, 0, 2, 0), (2, 0, 1, 0), (2, 0, 2, 0)]

from itertools import permutations

a = [1,2,3]
perm = permutations(a)
print(list(perm)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
perm = permutations(a, 2)
print(list(perm)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

from itertools import combinations

a = [1,2,3]
comb = combinations(a, 2)
print(list(comb)) # [(1, 2), (1, 3), (2, 3)]

from itertools import combinations_with_replacement

a = [1,2,3]
comb = combinations_with_replacement(a, 2)
print(list(comb)) # [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

from itertools import accumulate
import operator

a = [1,2,3]
acc = accumulate(a)
print(list(acc)) #[1,3,6]  acc[i] = a[i] + acc[i-1]
acc = accumulate(a, func = operator.mul)
print(list(acc)) #[1, 2, 6] acc[i] = a[i] * acc[i-1]
a = [1,3,2,0]
acc = accumulate(a, func = max)
print(list(acc)) #[1, 3, 3, 3] acc[i] = max(a[i], acc[i-1])

from itertools import groupby

def smallerthan3(x):
    return x < 3

a = [1,2,3,4]
gb = groupby(a, key = smallerthan3)
for k,v in gb:
    print(k, list(v))
#True [1, 2]
#False [3, 4]


#the same
gb = groupby(a, key = lambda x: x < 3)
for k,v in gb:
    print(k, list(v))


from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if(i == 20):
        break
#loop from 10 to 20 (without break if it would be infinity loop)

a = [1,2,3]
x = 0
for i in cycle(a):
    print(i)
    x+= 1
    if x == 10:
        break
# 1, 2, 3, 1, 2, 3, 1, 2...

x = 0
for i in repeat(1):
    print(i)
    x+= 1
    if x == 10:
        break
#1, 1, 1, 1....
for i in repeat(1,4):
    print(i)

#1,1,1,1


