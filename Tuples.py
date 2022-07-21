mytuple = ("cos", 1)
wierd_tuple = "cos", 1
print(mytuple)
print(wierd_tuple) # it s tuple too

mytuple = ("cos")
print(type(mytuple)) # it s not tuple

mytuple = ("cos",)
print(type(mytuple)) # it s tuple

mytuple = tuple(["cos", 1])
print(mytuple) # tuple form list

item = mytuple[0] #like list (-1 works too)

#mytuple[0] = "nic" Error!!

print(len(mytuple))

mytuple = ('a', 'p', 'p', 'l', 'e')

print(mytuple.count('p')) #num of p

print(mytuple.index('p')) #first index form left

mylist = list(mytuple)
print(mylist) #created list form tuple

sliced = mytuple [1:3]
print(sliced) #[::1] works too

mytuple = 1, 2, 3
el1, el2, el3 = mytuple #size must matching
print(el1)

mytuple = 0, 1, 2, 3 ,4, 5

first, *listinside, end = mytuple
print(first, listinside, end)

#Lists are larger than tuples
#Tuple is fasted to creat




