import json


def findComLeadUtil(emp1, emp2, parchild, root):
    if root == None:
        return [None, None]

    if root == emp1:
        return [root, None]

    if root == emp2:
        return [None, root]

    if root not in parchild.keys():
        return [None, None]

    founde1 = None
    founde2 = None

    for child in parchild[root]:
        emp1inroot, emp2inroot = findComLeadUtil(emp1, emp2, parchild, child)
        if emp1inroot != None and emp1inroot == emp2inroot:
            return [emp1inroot, emp2inroot]
        if emp1inroot:
            founde1 = emp1inroot
        if emp2inroot:
            founde2 = emp2inroot
        if founde1 and founde2:
            return [root, root]

    if founde1 != None:
        return [founde1, None]
    elif founde2 != None:
        return [None, founde2]
    else:
        return [None, None]


def findComLead(emp1, emp2, parchild, root):
    result = findComLeadUtil(emp1, emp2, parchild, root)
    if result[0] != None:
        return result[0]
    else:
        return result[1]


with open('org.json') as f:
    data = json.load(f)

head = data.pop('L0')[0]['name']

parchild = {head: []}

# go through all levels 1 by 1
for level in data.keys():
    # go through all pairs 1 by 1
    for pair in data[level]:

        # in dictionary make parent as key and children are list of values
        if pair['parent'] not in parchild.keys():
            parchild[pair['parent']] = []
        parchild[pair['parent']].append(pair['name'])

emp1 = int(input())
emp2 = int(input())

print(findComLead(emp1, emp2, parchild, head))
