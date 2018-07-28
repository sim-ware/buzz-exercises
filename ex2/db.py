import sqlite3


def getEvents(cursor):
    query = cursor.execute('SELECT * FROM events')
    result = [r for r in dict_gen(query)]
    return result


def getEventById(cursor, str_id):
    query = cursor.execute('SELECT * FROM events WHERE id=?', str(str_id))
    result = [r for r in dict_gen(query)]
    return result


def createEvent(cursor, start, end, label, category):
    cursor.execute("INSERT INTO events ('start', 'end', 'label', 'category') VALUES (?, ?, ?, ?);",
        (start, end, label, category))
    # query = cursor.execute('SELECT * FROM events WHERE start=?', start)
    query = cursor.execute('SELECT * FROM events ORDER BY id DESC LIMIT 1;')
    result = [r for r in dict_gen(query)]
    return result


def dict_gen(curs):
    field_names = [d[0].lower() for d in curs.description]
    while True:
        rows = curs.fetchmany()
        if not rows: return
        for row in rows:
            yield dict(zip(field_names, row))
