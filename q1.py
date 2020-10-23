import json

with open('jsoneg.json') as f:
    data = json.load(f)

root = data.pop('L0')[0]['name']

parchild = {root: []}

#go through all levels 1 by 1
for level in data.keys():
    # go through all pairs 1 by 1
    for pair in data[level]:

        # in dictionary make parent as key and children are list of values
        if pair['parent'] not in parchild.keys():
            parchild[pair['parent']] = []
        parchild[pair['parent']].append(pair['name'])

