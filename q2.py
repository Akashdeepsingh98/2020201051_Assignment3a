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

separators = ['-', '/', '.']


def prepare(date):
    if len(date) == 3:
        month = months[date[1][0:3].lower()]
        match = re.search(r'\d+', date[0])
        day = int(match.group())
        year = int(date[2])
        return [day, month, year]

    else:
        temp = date[0].split('/')
        print(temp)
    return date


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
