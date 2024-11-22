import sqlite3


def huldra(filename, *places):
    placeholders = ", ".join('?' for _ in places)

    db = sqlite3.connect(filename)
    cur = db.cursor()

    result = cur.execute(f"""SELECT DISTINCT Event.name, Brownies.being, Events.looks_like FROM events
                             JOIN Brownies ON Brownies.id = Events.being_id
                             JOIN Places ON Places.id = Events.place_id
                             WHERE Place.place IN ({placeholders}) AND Events.fraud == 1
                             ORDER BY Brownies.being ASC, Events.name DESC, Events.looks_like ASC""",
                         (places,)).fetchall()

    return result
