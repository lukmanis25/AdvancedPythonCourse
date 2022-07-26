import json

person = {'name': 'Lukas', 'hasChild': True, 'titles': ['engineer', 'programer']}

personJSON = json.dumps(person, indent= 4, sort_keys= True)
print(personJSON) #string json format (indent are spaces from new line)

with open('person.json', 'w') as file:
    json.dump(person, file, indent= 4)

person_loaded = json.loads(personJSON)
print(person_loaded) #string json to dict

with open('person.json', 'r') as file:
    person_loaded = json.load(file)
print(person_loaded)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Not serializable')

user = User('Lukas', 21)
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        else:
            return JSONEncoder.default(self, o)

user = User('Lukas', 22)
userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

user = User('Lukas', 23)
userJSON = UserEncoder().encode(user)
print(userJSON)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name = dct['name'], age = dct['age'])
    else:
        return dct

user = json.loads(userJSON, object_hook=decode_user)
print(user.name) #class object




