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


def checkisanc(i, pos, emp, empancs):
    result = []
    if empancs[pos][i-1] == emp:
        result.append(empancs[pos][i-2])
        for anc in empancs:
            if anc == empancs[pos]:
                result.append(1)
            else:
                result.append(len(anc)-1-(i-2))
        return result
    return None


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
    
    result = [None*3]
    result[0] = checkisanc(i, 0, emp1, [emp1anc, emp2anc])
    result[1] = checkisanc(i, 1, emp2, [emp1anc, emp2anc])

    for r in result:
        if r != None:
            return r

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

    result = [None*3]
    result[0] = checkisanc(i, 0, emp1, [emp1anc, emp2anc, emp3anc])
    result[1] = checkisanc(i, 1, emp2, [emp1anc, emp2anc, emp3anc])
    result[2] = checkisanc(i, 2, emp3, [emp1anc, emp2anc, emp3anc])

    for r in result:
        if r != None:
            return r

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

    result = [None*4]
    result[0] = checkisanc(i, 0, emp1, [emp1anc, emp2anc, emp3anc, emp4anc])
    result[1] = checkisanc(i, 1, emp2, [emp1anc, emp2anc, emp3anc, emp4anc])
    result[2] = checkisanc(i, 2, emp3, [emp1anc, emp2anc, emp3anc, emp4anc])
    result[3] = checkisanc(i, 3, emp4, [emp1anc, emp2anc, emp3anc, emp4anc])

    for r in result:
        if r != None:
            return r
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
    result = [None*5]
    result[0] = checkisanc(
        i, 0, emp1, [emp1anc, emp2anc, emp3anc, emp4anc, emp5anc])
    result[1] = checkisanc(
        i, 1, emp2, [emp1anc, emp2anc, emp3anc, emp4anc, emp5anc])
    result[2] = checkisanc(
        i, 2, emp3, [emp1anc, emp2anc, emp3anc, emp4anc, emp5anc])
    result[3] = checkisanc(
        i, 3, emp4, [emp1anc, emp2anc, emp3anc, emp4anc, emp5anc])
    result[4] = checkisanc(
        i, 4, emp5, [emp1anc, emp2anc, emp3anc, emp4anc, emp5anc])

    for r in result:
        if r != None:
            return r

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
