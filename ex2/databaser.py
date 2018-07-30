import sqlite3



class DataBaser(object):

    def __init__(self, db_filename):
        self.conn = sqlite3.connect(db_filename)
        self.cursor = self.conn.cursor()
        self.query = None
        self.result = None


    def getEvents(self):
        self.query = self.cursor.execute('SELECT * FROM events')
        self.result = [r for r in self.generateListOfDicts()]


    def getEventById(self, str_id):
        self.query = self.cursor.execute('SELECT * FROM events WHERE id=?', str(str_id))
        self.result = [r for r in self.generateListOfDicts()]


    def createEvent(self, start, end, label, category):
        self.cursor.execute("INSERT INTO events ('start', 'end', 'label', 'category') VALUES (?, ?, ?, ?);",
            (start, end, label, category))
        self.query = self.cursor.execute('SELECT * FROM events ORDER BY id DESC LIMIT 1;')
        self.result = [r for r in self.generateListOfDicts()]


    def removeEvent(self, str_id):
        self.cursor.execute("DELETE FROM events WHERE id=?", str(str_id))
        self.result = 'File successfully deleted.'


    def generateListOfDicts(self):
        field_names = [d[0].lower() for d in self.cursor.description]
        while True:
            rows = self.cursor.fetchmany()
            if not rows: return
            for row in rows:
                yield dict(zip(field_names, row))
