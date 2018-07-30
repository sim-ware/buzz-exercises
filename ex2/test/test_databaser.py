import unittest
import sys
sys.path.append("..")
from databaser import *



class TestDb(unittest.TestCase):

    def test_getEvents(self):
        db = DataBaser('test.db')
        #
        db.getEvents()
        # res = len(db.result)
        self.assertEqual(len(db.result), 5)
        #
        db.conn.close()


    def test_getEventById(self):
        db = DataBaser('test.db')
        #
        db.getEventById(1)
        res_one = db.result[0]['id']
        db.getEventById(3)
        res_two = db.result[0]['id']
        db.getEventById(5)
        res_three = db.result[0]['id']
        self.assertEqual(res_one, 1)
        self.assertEqual(res_two, 3)
        self.assertEqual(res_three, 5)
        #
        db.conn.close()


    def test_createEvent(self):
        db = DataBaser('test.db')
        #
        start = '2017-06-01T08:00:00Z'
        end = '2017-06-01T16:00:00Z'
        label = 'Comedy'
        category = 'black'
        db.createEvent(start, end, label, category)
        self.assertEqual(db.result[0]['label'], 'Comedy')
        self.assertEqual(db.result[0]['start'], '2017-06-01T08:00:00Z')
        #
        db.conn.close()


    def test_removeEvent(self):
        db = DataBaser('test.db')
        #
        start = '2017-06-01T08:00:00Z'
        end = '2017-06-01T16:00:00Z'
        label = 'Comedy'
        category = 'black'
        db.createEvent(start, end, label, category)
        db.removeEvent('6')
        # res = getEvents(conn.cursor())
        db.getEvents()
        self.assertEqual(len(db.result), 5)
        #
        db.conn.close()


    def test_generateListOfDicts(self):
        db = DataBaser('test.db')
        #
        query = db.cursor.execute('SELECT * FROM events')
        res = [r for r in db.generateListOfDicts()]
        self.assertEqual(str(type(res)), "<class 'list'>")
        #
        db.conn.close()


if __name__ == '__main__':
    unittest.main()
