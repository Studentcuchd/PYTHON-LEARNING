import json

with open("ex56.json","r") as reader:
    # dict1=json.load(reader)
    dict1=json.loads(reader.read())
print(dict1)