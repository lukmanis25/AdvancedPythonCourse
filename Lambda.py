#lambda arg: expression

add10 = lambda x: x+10
print(add10(5))

mult = lambda x,y: x*y
print(mult(3,4))

my_list = [(1,2), (2,-2), (-1,3)]
sorted_list = sorted(my_list)
print(sorted_list) #default by fist tuple ele
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list) #by second ele

a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))
#the same
c = [x*2 for x in a]
print(c)

b = filter(lambda x:x%2==0, a)
print(list(b)) #only even nums
#the same
c = [x for x in a if x%2 == 0]
print(c)

from functools import reduce

a = [1,2,3,4,5]
prod_a = reduce(lambda x,y: x*y, a)
print(prod_a) # 5! (1*2*3*4*5)