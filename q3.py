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
                length = (datetime.combine(key, interval[0])-start).seconds//60
                if length >= dur:
                    slotstart = start
                    while slotstart + timedelta(minutes=dur) <= datetime.combine(key, interval[0]):
                        slots.append(
                            [slotstart.time(), (slotstart+timedelta(minutes=dur)).time()])
                        slotstart = slotstart + timedelta(minutes=dur)
            start = datetime.combine(key, interval[1])
        if start != end:
            length = (end-start).seconds//60
            if length >= dur:
                slotstart = start
                while slotstart + timedelta(minutes=dur) <= end:
                    slots.append(
                        [slotstart.time(), (slotstart+timedelta(minutes=dur)).time()])
                    slotstart = slotstart + timedelta(minutes=dur)
        emp[key] = slots
    return emp


def matchFreeUtil(emp1, emp2, dur):
    numSlots = dur//30
    done = 0
    result = {}
    for day in emp1.keys():
        i = 0
        j = 0
        while i < len(emp1[day]) and j < len(emp2[day]):
            if datetime.combine(day, emp1[day][i][0]) > datetime.combine(day, emp2[day][j][0]):
                j += 1
            elif datetime.combine(day, emp1[day][i][0]) < datetime.combine(day, emp2[day][j][0]):
                i += 1
            else:
                done += 1
                if day not in result.keys():
                    result[day] = []
                if numSlots == 1:
                    result[day].append(emp1[day][i])
                    return result
                else:
                    if len(result[day]) == 0:
                        result[day].append(emp1[day][i])
                    else:
                        if result[day][-1][1] == emp1[day][i][0]:
                            result[day].append(emp1[day][i])
                        else:
                            done = 0
                            result[day] = []
                if done == numSlots:
                    return result
                i+=1
                j+=1
        while i < len(emp1[day]):
            if datetime.combine(day, emp1[day][i][0]) < datetime.combine(day, emp2[day][j][0]):
                i += 1
            else:
                done += 1
                if day not in result.keys():
                    result[day] = []
                if numSlots == 1:
                    result[day].append(emp1[day][i])
                    return result
                else:
                    if len(result[day]) == 0:
                        result[day].append(emp1[day][i])
                    else:
                        if result[day][-1][1] == emp1[day][i][0]:
                            result[day].append(emp1[day][i])
                        else:
                            done = 0
                            result[day] = []
                if done == numSlots:
                    return result
                i+=1
        while j < len(emp2[day]):
            if datetime.combine(day, emp1[day][i][0]) > datetime.combine(day, emp2[day][j][0]):
                j += 1
            else:
                done += 1
                if day not in result.keys():
                    result[day] = []
                if numSlots == 1:
                    result[day].append(emp1[day][i])
                    return result
                else:
                    if len(result[day]) == 0:
                        result[day].append(emp1[day][i])
                    else:
                        if result[day][-1][1] == emp1[day][i][0]:
                            result[day].append(emp1[day][i])
                        else:
                            done = 0
                            result[day] = []
                if done == numSlots:
                    return result
                j+=1
    return result


def matchFree(emp1, emp2, dur):
    result = matchFreeUtil(emp1, emp2, dur)
    for day in result.keys():
        start = result[day][0][0]
        end = result[day][-1][1]
        result[day] = [start, end]
    return result


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

#print(emp1)
#print(emp2)

emp1, emp2 = remUnnDat(emp1, emp2)

emp1 = getFreeTime(emp1, 30)
emp2 = getFreeTime(emp2, 30)

print(emp1)
print(emp2)

print('result is ')
print(matchFree(emp1, emp2, dur))
