import json


def findComLead(emp1, emp2, head, childpar):
    if emp1 == head or emp2 == head:
        print("Leader not found")
        return [0, 0, 0]
    emp1anc = [emp1]
    emp2anc = [emp2]

    while emp1anc[-1] != head or emp2anc[-1] != head:
        curhead1 = emp1anc[-1]
        curhead2 = emp2anc[-1]
        if curhead1 != head:
            emp1anc.append(childpar[curhead1])
        if curhead2 != head:
            emp2anc.append(childpar[curhead2])

    emp1anc.reverse()
    emp2anc.reverse()

    i = 0
    while i < len(emp1anc) and i < len(emp2anc) and emp1anc[i] == emp2anc[i]:
        i += 1

    if emp1anc[i-1] == emp1:
        return [emp1anc[i-2], 1, len(emp2anc)-1 - (i - 2)]

    if emp2anc[i-1] == emp2:
        return [emp2anc[i-2], len(emp1anc)-1 - (i - 2), 1]

    return [emp1anc[i-1], len(emp1anc)-1 - (i - 2), len(emp2anc)-1 - (i - 2)]


with open('org.json') as f:
    data = json.load(f)

head = data.pop('L0')[0]['name']

childpar = {}

for level in data.keys():
    for pair in data[level]:
        childpar[pair['name']] = pair['parent']

emp1, emp2 = input().strip().split()

result = findComLead(emp1, emp2, head, childpar)

if result!=[0,0,0]:
    print(result[0])
    print(str(result[0]) + ' is ' + str(result[1]) + ' levels above ' + str(emp1))
    print(str(result[0]) + ' is ' + str(result[2]) + ' levels above ' + str(emp2))
