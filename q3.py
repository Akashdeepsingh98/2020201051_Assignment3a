import ast
from datetime import datetime, timedelta


def myKey(t):
    return t[0]


def preprocess(emp):
    newemp = {}
    for dt in emp.keys():
        temp = datetime.strptime(dt, '%d/%m/%Y').date()
        newemp[temp] = []
        for interval in emp[dt]:
            start, end = interval.strip().split('-')
            start = datetime.strptime(start.strip(), '%I:%M%p').time()
            end = datetime.strptime(end.strip(), '%I:%M%p').time()
            newemp[temp].append([start, end])
        newemp[temp].sort(key=myKey)
    return newemp


def remUnnDat(emp1, emp2):
    for key in emp2.keys():
        if key not in emp1.keys():
            emp2.pop(key)

    for key in emp1.keys():
        if key not in emp2.keys():
            emp1.pop(key)

    return emp1, emp2


def getFreeTime(emp, dur):
    for key in emp.keys():
        start = datetime.combine(
            key, datetime.strptime('9:00AM', '%I:%M%p').time())
        end = datetime.combine(
            key, datetime.strptime('5:00PM', '%I:%M%p').time())
        slots = []
        for interval in emp[key]:
            if datetime.combine(key, interval[0]) == start:
                start = datetime.combine(key, interval[1])
                continue
            else:
                length = (end-start).min
                if length >= timedelta(minutes=dur):
                    slotstart = start
                    while slotstart + timedelta(minutes=dur) < end:
                        slots.append(
                            [slotstart, slotstart+timedelta(minutes=dur)])
                        slotstart = slotstart + timedelta(minutes=dur)
                    #slots.append([start, interval[0]])
            start = datetime.combine(key, interval[1])
        if start != end:
            slots.append([start, end])
        emp[key] = slots
    return emp


emp1 = {}
emp2 = {}

dur = float(input())
dur = dur*60  # converted to minutes

with open('Employee1.txt') as f:
    contents = f.read()
    emp1 = ast.literal_eval(contents)

with open('Employee2.txt') as f:
    contents = f.read()
    emp2 = ast.literal_eval(contents)

emp1 = emp1['Employee1']
emp2 = emp2['Employee2']

emp1 = preprocess(emp1)
emp2 = preprocess(emp2)

print(emp1)
print(emp2)

emp1, emp2 = remUnnDat(emp1, emp2)

emp1 = getFreeTime(emp1, dur)
emp2 = getFreeTime(emp2, dur)

print(emp1)
print(emp2)
