import json

with open('org.json') as f:
    data = json.load(f)

head = data.pop('L0')[0]['name']

childpar = {}

for level in data.keys():
    for pair in data[level]:
        childpar[pair['name']] = pair['parent']