import re
months = {
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'may': 5,
    'jun': 6,
    'jul': 7,
    'aug': 8,
    'sep': 9,
    'oct': 10,
    'nov': 11,
    'dec': 12
}

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

separators = ['-', '/', '.']


def prepare(date):
    if len(date) == 3:
        month = months[date[1][0:3].lower()]
        match = re.search(r'\d+', date[0])
        day = int(match.group())
        year = int(date[2])
        return [day, month, year]

    else:
        for sep in separators:
            temp = date[0].split(sep)
            if len(temp) == 3:
                temp = list(map(int, temp))
                break
        return temp


def distance(date):
    numdays = 0
    if date[1] > 2:
        numleap = date[2]//4 - date[2]//100 + date[2]//400
    else:
        numleap = (date[2]-1)//4 - (date[2]-1)//100 + (date[2]-1)//400

    numdays = date[2]*365 + numleap
    # num of days in months before
    for m in range(1, date[1]):
        numdays+=days[m-1]
    numdays+=date[0]

    return numdays


date1 = []
date2 = []
with open('date_calculator.txt') as f:
    date1 = f.readline()
    date2 = f.readline()

date1 = date1.strip().split()
date2 = date2.strip().split()
date1 = date1[1:]
date2 = date2[1:]

date1 = prepare(date1)
date2 = prepare(date2)
#print(date1)
#print(date2)
dist1 = distance(date1)
dist2 = distance(date2)
print(dist1)
print(dist2)

print(abs(dist1-dist2))
