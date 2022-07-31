def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()

val = next(g)
print(val) #1
val = next(g)
print(val) #2
#val = next(g)
#print(val) #3
#val = next(g)
#print(val) #Stop itteration

print(sum(g)) #3 bcs rest was used

def generetor1(num):
    print("start")
    while num > 0:
        yield num
        num -= 1

g = generetor1(4) # wont print anything !!

val = next(g) #print "start"
print(val) #print 4

val = next(g) # DONT print "start" !!
print(val) #print 3

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn_generator(10))) #45, save memory

def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

f = fib(30)
for i in f:
    print(i) #print fibonacci nums smaller than 30


#in () generetors !!
generetor = (i for i in range(10) if i %2 == 0)
# in [] list!!
l = [i for i in range(10) if i %2 == 0]