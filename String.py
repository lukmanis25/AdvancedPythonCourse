my_string = 'Hello'
print(my_string)

my_string = 'I\'m programmer'
print(my_string)

my_string = """Cos
enter cos"""
print(my_string)

my_string = """Cos \
bez enter cos"""
print(my_string)

#my_string[0] = 's' ERROR !!

my_string = my_string + " inny string"
print(my_string)

my_string = '     hello    dsd   '
my_string = my_string.strip()
print(my_string) # no spaces (but beetwen hello and dsd are spaces)

print(my_string.upper()) #upper cases
print(my_string.lower()) #lower cases

print(my_string.startswith("he")) #check if start with he
print(my_string.endswith("dsd")) #check if end with dsd

print(my_string.find('lo')) #index of substring start (-1 if cant find)

print(my_string.count("l")) #count ls

my_string = my_string.replace("dsd", "World")
print(my_string)

my_list = my_string.split()
print(my_list) # list of words

my_string = "Hello,world"
my_list = my_string.split(",")
print(my_list) # list of words separeted by ','

new_string = "".join(my_list)
print(new_string) #list to string (no spaces)
new_string = " ".join(my_list)
print(new_string) #list to string separeted by " "

#DONT DO LIKE BELOW bcs u create new string every time
my_list = ['a','a','a']
my_string = ''
for i in my_list:
    my_string += i
print(my_string)

#DO LIKE THAT
my_list = ['a','a','a']
my_string = ''
my_string = ''.join(my_list)
print(my_string)

#old
var = "Tom"
my_string = "My name is %s" % var
print(my_string) # %i for int, %f for float, %.2f float with 2 numbers after point

#new
var = "Tom"
my_string = "My name is {}".format(var)
print(my_string)
var = 3.1452
my_string = "My name is {:.3}".format(var)
print(my_string) # 3 numbers

#newest and the best
var = "Tom"
my_string = f"My name is {var}"
print(my_string)
var = 3.14
my_string = f"My name is {var*2}"
print(my_string)