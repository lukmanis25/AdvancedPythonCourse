mylist = list()
print(mylist) #empty

mylist = [1,2,3]
print(mylist[-1]) #last element

lenght = len(mylist)
print(lenght) # size

mylist.append(4)
print(mylist) #add at the end

mylist.insert(0,10)
print(mylist) #add at beg

x = mylist.pop()
print(mylist) #pop last

mylist.remove(10)
print(mylist) #remove el 10

mylist.reverse()
print(mylist)

mylist.clear()
print(mylist) # clear all

# mylist.sort
# newlist = sorted(mylist)

list1 = [1] * 5
print(list1) # 5 time [1,...,1]

list2 = [2,2]
list = list2 + list1
print(list) #merged

list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
sliced = list[1:5] # 1s is inclusive 5s is exclusive
print(sliced)

list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
sliced = list[:5] # from 0
print(sliced)

list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
sliced = list[1:] # to the end
print(sliced)

list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
sliced = list[::2] # 2 step
print(sliced)

list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
sliced = list[::-1] # reversed
print(sliced)

list = [1, 3, 5]
copy = list
copy[0] = 0
print(list) # changed oryginal !!

list = [1, 3, 5]
copy = list.copy()
copy[0] = 0
print(list) # changed only copy

list = [1, 3, 5]
copy = list[:] # list(list) works too
copy[0] = 0
print(list) # changed only copy

list = [1,2,3,4,5]
pov2 = [x*x for x in list]
print(pov2)