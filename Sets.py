myset = {1,2,3,1,2}
print(myset) #no duplicates printed

myset = set([1,2,3])
print(myset) #same like before

myset = set("Hello")
print(myset) #set of chars (duplicates deleted)

myset = {} #it s dictionary !!

myset = set() #it s set


myset.add(1)
print(myset) #add 1 time 1 and no error here

myset.remove(1)
print(myset) #removed, if not exist it s error

myset.add(1)
myset.discard(4)
print(myset) #no error if not found

myset.add(0)
myset.add(-1)
myset.pop()
print(myset) # del last

set1 = {1, 3, 5}
set2 = {2, 4, 6}
union = set1.union(set2)
print(union) #merge

intersection = set1.intersection(set2)
print(intersection) #elements in both sets

set1 = {1,2,3,4}
set2 = {3,4, 5}
diff = set1.difference(set2)
print(diff) #ele in set1 that arent in set2

symdiff = set1.symmetric_difference(set2)
print(symdiff) #ele in set1 or set2 but not in both


set1.intersection_update(set2)
print(set1) #if we use f.e set1.intersection_update(set2) it would change set1

set1 = {1, 2, 3}
set2 = {2, 3}
print(set1.issubset(set2)) # All ele in set1 are in set2 False
print(set1.issuperset(set2)) # All ele in set2 are in set1 True
print(set1.isdisjoint(set2)) # All ele in set2 are not in set1 False
print(set1.isdisjoint(set([7,8]))) # All ele in set2 are not in set1 True

# be careful with set1 = set2 bcs it s reference like in list (use set1 = set2.copy() or set1 = set(set2))

frozen = frozenset({1,2,3,4})
print(frozen)
#frozen.add(0) Error
#frozen.remove(1) Error
#Can t be modifed