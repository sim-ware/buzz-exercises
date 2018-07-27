import sqlite3


def getEvents(cursor):
    query = cursor.execute('SELECT * FROM events')
    result = []
    for row in query:
        result.append(row)
    return result


def getEventById(cursor, str_id):
    query = cursor.execute('SELECT * FROM events WHERE id=?', str(str_id))
    result = []
    for row in query:
        result.append(row)
    return result


def createEvent(cursor, start, end, label, category):
    cursor.execute("INSERT INTO events ('start', 'end', 'label', 'category') VALUES (?, ?, ?, ?);",
        (start, end, label, category))
    query = cursor.execute('SELECT * FROM events WHERE start=?', start)
    result = []
    for row in query:
        result.append(row)
    return result
