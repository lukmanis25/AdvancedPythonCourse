mydict = {"name": "lukas", "city": "Boston" }
print(mydict)

mydict = dict(name = "lukas", city = "Boston")
print(mydict) #same like befor

val = mydict["name"]
print(val)

mydict["email"] = "123@mail"
print(mydict) #add new el

del mydict["email"] #or mydict.pop("email")
print(mydict) #deleted email

mydict.popitem()
print(mydict) #del last

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["lastname"])
except:
    print("Error")

for key in mydict: #mydict.keys() do the same
    print(key)

for value in mydict.values(): #mydict.keys() do the same
    print(value)

for k, v in mydict.items():
    print(k,v)

copy = mydict
copy["name"] = "simon"
print(mydict) #original changed!!

copy = mydict.copy() # or dict(mydict)
copy["name"] = "lukas"
print(mydict) #only copy changed

copy["lastname"] = "smith"
mydict.update(copy)
print(mydict) #update or add value from copy

#tuple can be a key
#list cant 