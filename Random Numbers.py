import random

a = random.random()
print(a) #from 0 to 1 float

a = random.uniform(1,10)
print(a) #from 1 to 10 flaot

a = random.randint(1,10)
print(a) # from 1 to 10 int (10 is included)

a = random.randrange(1, 10 )
print(a) #from 1 to 10 int (10 is not included)

a = random.normalvariate(0,1)
print(a) #rozklad normalny

my_list = list("ABCDE")
print(my_list)
a = random.choice(my_list)
print(a) #random ele from list

a = random.sample(my_list, 3)
print(a) #3 unique ele as list

a = random.choices(my_list, k=3)
print(a) #3 random ele (can be not unique)

random.shuffle(my_list)
print(my_list) #random sequence

random.seed(1)
print(random.randrange(1,10))
print(random.random())
random.seed(1)
print(random.randrange(1,10))
print(random.random())
#the same value

random.seed(1)
print(random.randrange(1,10))
print(random.random())
random.seed(2)
print(random.randrange(1,10))
print(random.random())
random.seed(1)
print(random.randrange(1,10))
print(random.random())
random.seed(2)
print(random.randrange(1,10))
print(random.random())
#all 1 seeds get the same values and 2 too


#True random nums
import secrets

a = secrets.randbelow(10)
print(a) #from 1 to 10 (10 exclusive)

a = secrets.randbits(4)
print(a) #random int on 4 bits (max 15


#import numpy as np

#a = np.random.rand(3)  #random vector with 3 elements <0,1)

#a = np.random.rand(3,3)  #random matrix with 3x3 elements <0,1)

#a = np.random.randint(0,10, 3)  #random vector with 3 elements <0,10)

#a = np.random.randint(0,10, (3,3))  #random matrix with 3x3 elements <0,10)

#a = np.random.shuffle(a) #random swap rows

#np.random.seed(1) #seeds like on random








