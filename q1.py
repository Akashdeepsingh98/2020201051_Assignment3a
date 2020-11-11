import json


def checkheads(curhead, head, empanc, childpar):
    if curhead == head:
        empanc.append(childpar[curhead])


def checkallequal(emps, head):
    for emp in emps:
        if emp != head:
            return False
    return True


def checknotallequal(empancs, head):
    for empanc in empancs:
        if empanc != head:
            return True
    return False


def canincr(i, empancs):
    temp = empancs[0][i]
    for empanc in empancs:
        if i >= len(empanc) or empanc[i] != temp:
            return False
    return True


def findComLead2(emp1, emp2, head, childpar):
    if checkallequal([emp1, emp2], head):
        print("Leader not found")
        return 0
    emp1anc = [emp1]
    emp2anc = [emp2]

    while checknotallequal([emp1anc[-1], emp2anc[-1]], head):
        curhead1 = emp1anc[-1]
        curhead2 = emp2anc[-1]
        checkheads(curhead1, head, emp1anc, childpar)
        checkheads(curhead2, head, emp2anc, childpar)
        
    emp1anc.reverse()
    emp2anc.reverse()

    i = 0
    while canincr(i, [emp1anc, emp2anc]):
        i += 1

    if emp1anc[i-1] == emp1:
        return [emp1anc[i-2], 1, len(emp2anc)-1 - (i - 2)]

    if emp2anc[i-1] == emp2:
        return [emp2anc[i-2], len(emp1anc)-1 - (i - 2), 1]

    return [emp1anc[i-1], len(emp1anc)-1 - (i - 2), len(emp2anc)-1 - (i - 2)]


def findComLead3(emp1, emp2, emp3, head, childpar):
    if checkallequal([emp1, emp2, emp3], head):
        print('Leader not found')
        return 0

    emp1anc = [emp1]
    emp2anc = [emp2]
    emp3anc = [emp3]

    while checknotallequal([emp1anc[-1], emp2anc[-1], emp3anc[-1]], head):
        curhead1 = emp1anc[-1]
        curhead2 = emp2anc[-1]
        curhead3 = emp3anc[-1]
        checkheads(curhead1, head, emp1anc, childpar)
        checkheads(curhead2, head, emp2anc, childpar)
        checkheads(curhead3, head, emp3anc, childpar)

    emp1anc.reverse()
    emp2anc.reverse()
    emp3anc.reverse()

    i = 0
    while canincr(i, [emp1anc, emp2anc, emp3anc]):
        i += 1

    if emp1anc[i-1] == emp1:
        return [emp1anc[i-2], 1, len(emp2anc)-1-(i-2), len(emp3anc)-1-(i-2)]

    if emp2anc[i-1] == emp2:
        return [emp2anc[i-2], len(emp1anc)-1-(i-2), 1, len(emp3anc)-1-(i-2)]

    if emp3anc[i-1] == emp3:
        return [emp3anc[i-2], len(emp1anc)-1-(i-2), len(emp2anc)-1-(i-2), 1]

    return [emp1anc[i-1], len(emp1anc)-1-(i-2), len(emp2anc)-1-(i-2), len(emp3anc)-1-(i-2)]


def findComLead4(emp1, emp2, emp3, emp4, head, childpar):
    if checkallequal([emp1, emp2, emp3, emp4], head):
        print('Leader not found')
        return 0

    emp1anc = [emp1]
    emp2anc = [emp2]
    emp3anc = [emp3]
    emp4anc = [emp4]

    while checknotallequal([emp1anc[-1], emp2anc[-1], emp3anc[-1], emp4anc[-1]], head):
        curhead1 = emp1anc[-1]
        curhead2 = emp2anc[-1]
        curhead3 = emp3anc[-1]
        curhead4 = emp4anc[-1]
        checkheads(curhead1, head, emp1anc, childpar)
        checkheads(curhead2, head, emp2anc, childpar)
        checkheads(curhead3, head, emp3anc, childpar)
        checkheads(curhead4, head, emp4anc, childpar)

    emp1anc.reverse()
    emp2anc.reverse()
    emp3anc.reverse()
    emp4anc.reverse()

    i = 0
    while canincr(i, [emp1anc, emp2anc, emp3anc, emp4anc]):
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
    if checkallequal([emp1, emp2, emp3, emp4, emp5], head):
        print('Leader not found')
        return 0

    emp1anc = [emp1]
    emp2anc = [emp2]
    emp3anc = [emp3]
    emp4anc = [emp4]
    emp5anc = [emp5]

    while checknotallequal([emp1anc[-1], emp2anc[-1], emp3anc[-1], emp4anc[-1], emp5anc[-1]], head):
        curhead1 = emp1anc[-1]
        curhead2 = emp2anc[-1]
        curhead3 = emp3anc[-1]
        curhead4 = emp4anc[-1]
        curhead5 = emp5anc[-1]
        checkheads(curhead1, head, emp1anc, childpar)
        checkheads(curhead2, head, emp2anc, childpar)
        checkheads(curhead3, head, emp3anc, childpar)
        checkheads(curhead4, head, emp4anc, childpar)
        checkheads(curhead5, head, emp5anc, childpar)
    emp1anc.reverse()
    emp2anc.reverse()
    emp3anc.reverse()
    emp4anc.reverse()
    emp5anc.reverse()

    i = 0
    while canincr(i, [emp1anc, emp2anc, emp3anc, emp4anc, emp5anc]):
        i += 1

    if emp1anc[i-1] == emp1:
        return [emp1anc[i-2], 1, len(emp2anc)-1-(i-2), len(emp3anc)-1-(i-2), len(emp4anc)-1-(i-2), len(emp5anc)-1-(i-2)]

    elif emp2anc[i-1] == emp2:
        return [emp2anc[i-2], len(emp1anc)-1-(i-2), 1, len(emp3anc)-1-(i-2), len(emp4anc)-1-(i-2), len(emp5anc)-1-(i-2)]

    elif emp3anc[i-1] == emp3:
        return [emp3anc[i-2], len(emp1anc)-1-(i-2), len(emp2anc)-1-(i-2), 1, len(emp4anc)-1-(i-2), len(emp5anc)-1-(i-2)]

    elif emp4anc[i-1] == emp4:
        return [emp4anc[i-2], len(emp1anc)-1-(i-2), len(emp2anc)-1-(i-2), len(emp3anc)-1-(i-2), 1, len(emp5anc)-1-(i-2)]

    elif emp5anc[i-1] == emp5:
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
            print('common leader: ' + result[0])
            print('leader ' + str(result[0]) + ' is ' + str(result[1]-1) +
                  ' levels above employee ' + str(bunch[1]))
            print('leader ' + str(result[0]) + ' is ' + str(result[2]-1) +
                  ' levels above employee ' + str(bunch[2]))
    elif int(bunch[0]) == 3:
        result = findComLead3(bunch[1], bunch[2], bunch[3], head, childpar)
        if result != 0:
            print('common leader: ' + result[0])
            print('leader ' + str(result[0]) + ' is ' + str(result[1]-1) +
                  ' levels above employee ' + str(bunch[1]))
            print('leader ' + str(result[0]) + ' is ' + str(result[2]-1) +
                  ' levels above employee ' + str(bunch[2]))
            print('leader ' + str(result[0]) + ' is ' + str(result[3]-1) +
                  ' levels above employee ' + str(bunch[3]))

    elif int(bunch[0]) == 4:
        result = findComLead4(bunch[1], bunch[2],
                              bunch[3], bunch[4], head, childpar)
        if result != 0:
            print('common leader: ' + result[0])
            print('leader ' + str(result[0]) + ' is ' + str(result[1]-1) +
                  ' levels above employee ' + str(bunch[1]))
            print('leader ' + str(result[0]) + ' is ' + str(result[2]-1) +
                  ' levels above employee ' + str(bunch[2]))
            print('leader ' + str(result[0]) + ' is ' + str(result[3]-1) +
                  ' levels above employee ' + str(bunch[3]))
            print('leader ' + str(result[0]) + ' is ' + str(result[4]-1) +
                  ' levels above employee ' + str(bunch[4]))
    elif int(bunch[0]) == 5:
        result = findComLead5(
            bunch[1], bunch[2], bunch[3], bunch[4], bunch[5], head, childpar)
        if result != 0:
            print('common leader: ' + result[0])
            print('leader ' + str(result[0]) + ' is ' + str(result[1]-1) +
                  ' levels above employee ' + str(bunch[1]))
            print('leader ' + str(result[0]) + ' is ' + str(result[2]-1) +
                  ' levels above employee ' + str(bunch[2]))
            print('leader ' + str(result[0]) + ' is ' + str(result[3]-1) +
                  ' levels above employee ' + str(bunch[3]))
            print('leader ' + str(result[0]) + ' is ' + str(result[4]-1) +
                  ' levels above employee ' + str(bunch[4]))
            print('leader ' + str(result[0]) + ' is ' + str(result[5]-1) +
                  ' levels above employee ' + str(bunch[5]))
