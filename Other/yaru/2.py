import sqlite3

names = input().split()
placeholders = ', '.join(['?' for _ in names])
n = int(input())

db = sqlite3.connect('blizzard.db')
cur = db.cursor()

result = cur.execute(f"""SELECT name, place FROM Meetings
                         WHERE alien IN ({placeholders}) AND unusual >= ?""", (*names, n)).fetchall()

names = list(set([elem[0] for elem in result]))
names.sort()
print(", ".join(names))
places = list(set([elem[1] for elem in result]))
places.sort()
print(", ".join(places))
