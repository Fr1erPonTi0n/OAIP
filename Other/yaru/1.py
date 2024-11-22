import csv
import sys

result = [['no', 'place', 'deal', 'magic']]
lines = [line.split(', ') for line in list(map(str.strip, sys.stdin))]

count = 1
for line in lines:
    if int(line[-1]) and line[0] == 'Nisse':
        result.append([count, line[1], line[2], (len(line[1]) * len(line)) // 3])
        count += 1

with open("christmas.csv", "w", encoding='utf-8') as f:
    w = csv.writer(f, delimiter=';')
    w.writerows(result)
