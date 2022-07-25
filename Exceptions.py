x = 10

#x = -5
#throw exception
if x < 0:
    raise Exception('x should be positive')

#throw AssertionError
#x = -5
assert (x >= 0), 'x should be positive'


#doesnt throw anything, just print on console
try:
    a = 5/0
except:
    print('Something went wrong')

#write exceptions name
try:
    a = 5/0
except Exception as e:
    print(e)


try:
    a = 5/1
    b = 5 + 'a'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('used every time even if there was expection or not')

class ValueTooLargeException(Exception):
    pass
x = 101
def test(x):
    if x > 100:
        raise ValueTooLargeException('x is too large')

try:
    test(x)
except ValueTooLargeException as e:
    print(e)

#x is too large on console

class ValueTooSmallExpection(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test2(x):
    if x < 5:
        raise ValueTooSmallExpection('value too small', x)

x = 1
try:
    test2(1)
except ValueTooSmallExpection as e:
    print(e.message, e.value)

#value too small 1