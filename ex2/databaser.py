import sqlite3



# class DataBaser(object):
#     class_var = 1
#
#     def __init__(self, db_filename):
#         self.conn = sqlite3.connect(db_filename)
# self.cursor = conn.cursor()
# self.query = None
# self.result = None


def getEvents(cursor):
    query = cursor.execute('SELECT * FROM events')
    result = [r for r in generateListOfDicts(query)]
    return result


def getEventById(cursor, str_id):
    query = cursor.execute('SELECT * FROM events WHERE id=?', str(str_id))
    result = [r for r in generateListOfDicts(query)]
    return result


def createEvent(cursor, start, end, label, category):
    cursor.execute("INSERT INTO events ('start', 'end', 'label', 'category') VALUES (?, ?, ?, ?);",
        (start, end, label, category))
    query = cursor.execute('SELECT * FROM events ORDER BY id DESC LIMIT 1;')
    result = [r for r in generateListOfDicts(query)]
    return result


def removeEvent(cursor, str_id):
    cursor.execute("DELETE FROM events WHERE id=?", str(str_id))
    return 'File successfully deleted.'


def generateListOfDicts(cursor):
    field_names = [d[0].lower() for d in cursor.description]
    while True:
        rows = cursor.fetchmany()
        if not rows: return
        for row in rows:
            yield dict(zip(field_names, row))
