import os
import ast
from datetime import datetime


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


if __name__ == '__main__':
    employeelist = readFiles('employees')
    print(employeelist)

    print()
    employeelist = preprocess(employeelist)
    print(employeelist)

    print()
    employeelist = getFreeSlots(employeelist)
    print(employeelist)
