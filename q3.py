import ast
from datetime import datetime


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

emp1 = {}
emp2 = {}
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

#emp1 = getFreeTime(emp1)
#emp2 = getFreeTime(emp2)