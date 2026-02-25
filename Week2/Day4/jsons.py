# loads and dumps
# (s, works with strings) use when you receive a json from an API response or need to send a json in a request

#load and dump
# (no s, works with files) use when you're reading from or writing to a .json file on disk
# always use indent = 2 when loading files or printing to console

import json

## Python string -> Python dict (loads = loads from string)

json_string = '{"name" : "Alice", "age" : "30", "languages" : ["Python", "Javascript"]}'
data =json.loads(json_string)

print(f"Type {type(data)}")
print(f"Name: {data['name']}")
print(f"Languages: {data['languages']}")

person = {"name" : "Bob", "age" : 25, "active" : True, "score" : None}

ugly = json.dumps(person)
print(f"Ugly:  {ugly}")