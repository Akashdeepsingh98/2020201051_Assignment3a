import os
import ast
from datetime import datetime, timedelta


def prepEmp(employee):
    empname = list(employee.keys())[0]
    dictforemp = {}
    dictforemp[empname] = {}
    for aday in employee[empname].keys():
        newdaylabel = datetime.strptime(aday, '%d/%m/%Y')
        newlist = []
        for slot in employee[empname][aday]:
            start, end = slot.split('-')
            newstart = datetime.strptime(start.strip(), '%I:%M%p')
            newend = datetime.strptime(end.strip(), '%I:%M%p')
            newlist.append([newstart, newend])
        dictforemp[empname][newdaylabel] = newlist
    return dictforemp


def preprocess(employeelist):
    result = []
    for employee in employeelist:
        result.append(prepEmp(employee))
    return result


def readFiles(dirname):
    # get names of all files
    listfiles = [name for name in os.listdir(dirname)]

    # read contents and store in list
    result = []
    for name in listfiles:
        with open(dirname + '/' + name) as f:
            contents = f.read()
            result.append(ast.literal_eval(contents))
    return result


def getEmpFreeSlots(employee):
    empname = list(employee.keys())[0]
    dictforemp = {}
    dictforemp[empname] = {}
    for aday in employee[empname].keys():
        newlist = []
        daystart = datetime.strptime('9:00AM', '%I:%M%p')
        dayend = datetime.strptime('5:00PM', '%I:%M%p')
        start = daystart
        for busyslot in employee[empname][aday]:
            if busyslot[0] == start:
                start = busyslot[1]
                continue
            else:
                newlist.append([start, busyslot[0]])
                start = busyslot[1]
        if employee[empname][aday][-1][1] != dayend:
            newlist.append([employee[empname][aday][-1][1], dayend])
        dictforemp[empname][aday] = newlist
    return dictforemp


def getFreeSlots(employeelist):
    result = []
    for employee in employeelist:
        result.append(getEmpFreeSlots(employee))
    return result


def isTimeOverlap(start1, end1, start2, end2):
    if start1 < start2 and start2 < end1 and end1 < end2:
        return True

    if start2 < start1 and start1 < end2 and end2 < end1:
        return True

    if start2 <= start1 and end1 <= end2:
        return True

    if start1 <= start2 and end2 <= end1:
        return True

    return False


def getFirstFreeSlot2(employeelist, duration):

    emp1name = list(employeelist[0].keys())[0]

    for emp1day in employeelist[0][emp1name].keys():
        emp2name = list(employeelist[1].keys())[0]
        for emp2day in employeelist[1][emp2name].keys():
            if emp1day == emp2day:
                for emp1slot in employeelist[0][emp1name][emp1day]:
                    for emp2slot in employeelist[1][emp2name][emp2day]:
                        if isTimeOverlap(emp1slot[0], emp1slot[1], emp2slot[0], emp2slot[1]):
                            temp = [emp1slot[0], emp1slot[1],
                                    emp2slot[0], emp2slot[1]]
                            temp.sort()
                            start = temp[1]
                            end = temp[2]
                            delta = end - start
                            if (delta.total_seconds()) / 60 >= duration:
                                return [start, start + timedelta(minutes=duration)]
    return 'no slot available'


def getFirstFreeSlot3(employeelist, duration):
    emp1name = list(employeelist[0].keys())[0]

    for emp1day in employeelist[0][emp1name].keys():
        emp2name = list(employeelist[1].keys())[0]
        for emp2day in employeelist[1][emp2name].keys():
            if emp1day == emp2day:
                for emp1slot in employeelist[0][emp1name][emp1day]:
                    for emp2slot in employeelist[1][emp2name][emp2day]:
                        if isTimeOverlap(emp1slot[0], emp1slot[1], emp2slot[0], emp2slot[1]):
                            temp12 = [emp1slot[0], emp1slot[1],
                                      emp2slot[0], emp2slot[1]]
                            temp12.sort()
                            start12 = temp12[1]
                            end12 = temp12[2]
                            delta12 = end12-start12
                            if(delta12.total_seconds()/60) >= duration:
                                emp3name = list(employeelist[2].keys())[0]
                                for emp3day in employeelist[2][emp3name].keys():
                                    if emp1day == emp3day:
                                        for emp3slot in employeelist[2][emp3name][emp3day]:
                                            if isTimeOverlap(start12, end12, emp3slot[0], emp3slot[1]):
                                                temp123 = [
                                                    start12, end12, emp3slot[0], emp3slot[1]]
                                                temp123.sort()
                                                start123 = temp123[1]
                                                end123 = temp123[2]
                                                delta123 = end123-start123
                                                if (delta123.total_seconds()/60) >= duration:
                                                    return [start123, start123 + timedelta(minutes=duration)]


if __name__ == '__main__':
    employeelist = readFiles('employees')
    print(employeelist)

    print()
    employeelist = preprocess(employeelist)
    print(employeelist)

    print()
    employeelist = getFreeSlots(employeelist)
    print(employeelist)

    print(getFirstFreeSlot3(employeelist, 30))
