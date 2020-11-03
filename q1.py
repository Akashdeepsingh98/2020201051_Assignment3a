import json


def findComLead2(emp1, emp2, head, childpar):
    if emp1 == head or emp2 == head:
        print("Leader not found")
        return 0
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


def findComLead3(emp1, emp2, emp3, head, childpar):
    if emp1 == head or emp2 == head or emp3 == head:
        print('Leader not found')
        return 0

    emp1anc = [emp1]
    emp2anc = [emp2]
    emp3anc = [emp3]

    while emp1anc[-1] != head or emp2anc[-1] != head or emp3anc[-1] != head:
        curhead1 = emp1anc[-1]
        curhead2 = emp2anc[-1]
        curhead3 = emp3anc[-1]
        if curhead1 != head:
            emp1anc.append(childpar[curhead1])
        if curhead2 != head:
            emp2anc.append(childpar[curhead2])
        if curhead3 != head:
            emp3anc.append(childpar[curhead3])

    emp1anc.reverse()
    emp2anc.reverse()
    emp3anc.reverse()

    i = 0
    while i < len(emp1anc) and i < len(emp2anc) and i < len(emp3anc) and emp1anc[i] == emp2anc[i] and emp1anc[i] == emp3anc[i]:
        i += 1

    if emp1anc[i-1] == emp1:
        return [emp1anc[i-2], 1, len(emp2anc)-1-(i-2), len(emp3anc)-1-(i-2)]

    if emp2anc[i-1] == emp2:
        return [emp2anc[i-2], len(emp1anc)-1-(i-2), 1, len(emp3anc)-1-(i-2)]

    if emp3anc[i-1] == emp3:
        return [emp3anc[i-2], len(emp1anc)-1-(i-2), len(emp2anc)-1-(i-2), 1]

    return [emp1anc[i-1], len(emp1anc)-1-(i-2), len(emp2anc)-1-(i-2), len(emp3anc)-1-(i-2)]


def findComLead4(emp1, emp2, emp3, emp4, head, childpar):
    if emp1 == head or emp2 == head or emp3 == head or emp4 == head:
        print('Leader not found')
        return 0

    emp1anc = [emp1]
    emp2anc = [emp2]
    emp3anc = [emp3]
    emp4anc = [emp4]

    while emp1anc[-1] != head or emp2anc[-1] != head or emp3anc[-1] != head or emp4anc[-1] != head:
        curhead1 = emp1anc[-1]
        curhead2 = emp2anc[-1]
        curhead3 = emp3anc[-1]
        curhead4 = emp4anc[-1]
        if curhead1 != head:
            emp1anc.append(childpar[curhead1])
        if curhead2 != head:
            emp2anc.append(childpar[curhead2])
        if curhead3 != head:
            emp3anc.append(childpar[curhead3])
        if curhead4 != head:
            emp4anc.append(childpar[curhead4])

    emp1anc.reverse()
    emp2anc.reverse()
    emp3anc.reverse()
    emp4anc.reverse()

    i = 0
    while i < len(emp1anc) and i < len(emp2anc) and i < len(emp3anc) and i < len(emp4anc) and emp1anc[i] == emp2anc[i] and emp1anc[i] == emp3anc[i] and emp1anc[i] == emp4anc[i]:
        i += 1

    if emp1anc[i-1] == emp1:
        return [emp1anc[i-2], 1, len(emp2anc)-1-(i-2), len(emp3anc)-1-(i-2), len(emp4anc)-1-(i-2)]

    if emp2anc[i-1] == emp2:
        return [emp2anc[i-2], len(emp1anc)-1-(i-2), 1, len(emp3anc)-1-(i-2), len(emp4anc)-1-(i-2)]

    if emp3anc[i-1] == emp3:
        return [emp3anc[i-2], len(emp1anc)-1-(i-2), len(emp2anc)-1-(i-2), 1, len(emp4anc)-1-(i-2)]

    if emp4anc[i-1] == emp4:
        return [emp4anc[i-2], len(emp1anc)-1-(i-2), len(emp2anc)-1-(i-2), len(emp3anc)-1-(i-2), 1]

    return [emp1anc[i-1], len(emp1anc)-1-(i-2), len(emp2anc)-1-(i-2), len(emp3anc)-1-(i-2), len(emp4anc)-1-(i-2)]


def findComLead5(emp1, emp2, emp3, emp4, emp5, head, childpar):
    if emp1 == head or emp2 == head or emp3 == head or emp4 == head or emp5 == head:
        print('Leader not found')
        return 0

    emp1anc = [emp1]
    emp2anc = [emp2]
    emp3anc = [emp3]
    emp4anc = [emp4]
    emp5anc = [emp5]

    while emp1anc[-1] != head or emp2anc[-1] != head or emp3anc[-1] != head or emp4anc[-1] != head or emp5anc[-1] != head:
        curhead1 = emp1anc[-1]
        curhead2 = emp2anc[-1]
        curhead3 = emp3anc[-1]
        curhead4 = emp4anc[-1]
        curhead5 = emp5anc[-1]
        if curhead1 != head:
            emp1anc.append(childpar[curhead1])
        if curhead2 != head:
            emp2anc.append(childpar[curhead2])
        if curhead3 != head:
            emp3anc.append(childpar[curhead3])
        if curhead4 != head:
            emp4anc.append(childpar[curhead4])
        if curhead5 != head:
            emp5anc.append(childpar[curhead5])
    emp1anc.reverse()
    emp2anc.reverse()
    emp3anc.reverse()
    emp4anc.reverse()
    emp5anc.reverse()

    i = 0
    while i < len(emp1anc) and i < len(emp2anc) and i < len(emp3anc) and i < len(emp4anc) and i < len(emp5anc) and emp1anc[i] == emp2anc[i] and emp1anc[i] == emp3anc[i] and emp1anc[i] == emp4anc[i] and emp1anc[i] == emp5anc[i]:
        i += 1

    if emp1anc[i-1] == emp1:
        return [emp1anc[i-2], 1, len(emp2anc)-1-(i-2), len(emp3anc)-1-(i-2), len(emp4anc)-1-(i-2), len(emp5anc)-1-(i-2)]

    if emp2anc[i-1] == emp2:
        return [emp2anc[i-2], len(emp1anc)-1-(i-2), 1, len(emp3anc)-1-(i-2), len(emp4anc)-1-(i-2), len(emp5anc)-1-(i-2)]

    if emp3anc[i-1] == emp3:
        return [emp3anc[i-2], len(emp1anc)-1-(i-2), len(emp2anc)-1-(i-2), 1, len(emp4anc)-1-(i-2), len(emp5anc)-1-(i-2)]

    if emp4anc[i-1] == emp4:
        return [emp4anc[i-2], len(emp1anc)-1-(i-2), len(emp2anc)-1-(i-2), len(emp3anc)-1-(i-2), 1, len(emp5anc)-1-(i-2)]

    if emp5anc[i-1] == emp5:
        return [emp5anc[i-2], len(emp1anc)-1-(i-2), len(emp2anc)-1-(i-2), len(emp3anc)-1-(i-2), len(emp4anc)-1-(i-2), 1]

    return [emp1anc[i-1], len(emp1anc)-1-(i-2), len(emp2anc)-1-(i-2), len(emp3anc)-1-(i-2), len(emp4anc)-1-(i-2), len(emp5anc)-1-(i-2)]


if __name__ == '__main__':
    with open('org.json') as f:
        data = json.load(f)

    head = data.pop('L0')[0]['name']

    childpar = {}

    for level in data.keys():
        for pair in data[level]:
            childpar[pair['name']] = pair['parent']

    bunch = input().strip().split()

    if int(bunch[0]) == 2:
        result = findComLead2(bunch[1], bunch[2], head, childpar)
        if result != 0:
            print(result[0])
            print(str(result[0]) + ' is ' + str(result[1]-1) +
                  ' levels above ' + str(bunch[1]))
            print(str(result[0]) + ' is ' + str(result[2]-1) +
                  ' levels above ' + str(bunch[2]))
    elif int(bunch[0]) == 3:
        result = findComLead3(bunch[1], bunch[2], bunch[3], head, childpar)
        if result != 0:
            print(result[0])
            print(str(result[0]) + ' is ' + str(result[1]-1) +
                  ' levels above ' + str(bunch[1]))
            print(str(result[0]) + ' is ' + str(result[2]-1) +
                  ' levels above ' + str(bunch[2]))
            print(str(result[0]) + ' is ' + str(result[3]-1) +
                  ' levels above ' + str(bunch[3]))

    elif int(bunch[0]) == 4:
        result = findComLead4(bunch[1], bunch[2],
                              bunch[3], bunch[4], head, childpar)
        if result != 0:
            print(result[0])
            print(str(result[0]) + ' is ' + str(result[1]-1) +
                  ' levels above ' + str(bunch[1]))
            print(str(result[0]) + ' is ' + str(result[2]-1) +
                  ' levels above ' + str(bunch[2]))
            print(str(result[0]) + ' is ' + str(result[3]-1) +
                  ' levels above ' + str(bunch[3]))
            print(str(result[0]) + ' is ' + str(result[4]-1) +
                  ' levels above ' + str(bunch[4]))
    elif int(bunch[0]) == 5:
        result = findComLead5(
            bunch[1], bunch[2], bunch[3], bunch[4], bunch[5], head, childpar)
        if result != 0:
            print(result[0])
            print(str(result[0]) + ' is ' + str(result[1]-1) +
                  ' levels above ' + str(bunch[1]))
            print(str(result[0]) + ' is ' + str(result[2]-1) +
                  ' levels above ' + str(bunch[2]))
            print(str(result[0]) + ' is ' + str(result[3]-1) +
                  ' levels above ' + str(bunch[3]))
            print(str(result[0]) + ' is ' + str(result[4]-1) +
                  ' levels above ' + str(bunch[4]))
            print(str(result[0]) + ' is ' + str(result[5]-1) +
                  ' levels above ' + str(bunch[5]))
