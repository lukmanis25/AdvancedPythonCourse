def start_end_decorator(func):

    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

print_name()
#start
#Alex
#end


#With arg
def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return wrapper

@start_end_decorator
def add5(x):
    return x+5

r = add5(10)
print(r) #print None


#Save result
def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x+5

r = add5(10)
print(r)


#Info about add5

import functools
def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x+5

print(help(add5))
print(add5.__name__) #print add5 bcs we add functools,wraps


#GOOD DECORATOR TEMPLATE

import functools
def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #Do befor...
        result = func(*args, **kwargs)
        #Do after...
        return result
    return wrapper


import functools

def repeat(num_times):
    def repeat_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return repeat_decorator



@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet('Lukas') #print 3 times

#@decorator1
#@decorator2
#def fun()
#decoretor 1 will be first

#Class decoretors for save state

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()
say_hello()





