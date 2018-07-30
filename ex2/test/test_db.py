import unittest
import sys
sys.path.append("..")
# from app import object
from databaser import *



class TestDb(unittest.TestCase):

    def test_getEvents(self):
        conn = sqlite3.connect('test.db')
        #
        res = getEvents(conn.cursor())
        self.assertEqual(len(res), 5)
        #
        conn.close()


    def test_getEventById(self):
        conn = sqlite3.connect('test.db')
        #
        res = getEvents(conn.cursor())
        res_one = res[0]['id']
        res_two = res[1]['id']
        res_three = res[2]['id']
        self.assertEqual(res_one, 1)
        self.assertEqual(res_two, 2)
        self.assertEqual(res_three, 3)
        #
        conn.close()


    def test_createEvent(self):
        conn = sqlite3.connect('test.db')
        #
        start = '2017-06-01T08:00:00Z'
        end = '2017-06-01T16:00:00Z'
        label = 'Comedy'
        category = 'black'
        res_one = createEvent(conn.cursor(), start, end, label, category)
        self.assertEqual(res_one[0]['label'], 'Comedy')
        self.assertEqual(res_one[0]['start'], '2017-06-01T08:00:00Z')
        #
        conn.close()


    def test_removeEvent(self):
        conn = sqlite3.connect('test.db')
        #
        start = '2017-06-01T08:00:00Z'
        end = '2017-06-01T16:00:00Z'
        label = 'Comedy'
        category = 'black'
        res_one = createEvent(conn.cursor(), start, end, label, category)
        removeEvent(conn.cursor(), '6')
        res = getEvents(conn.cursor())
        self.assertEqual(len(res), 5)
        #
        conn.close()


    def test_generateListOfDicts(self):
        conn = sqlite3.connect('test.db')
        #
        query = conn.cursor().execute('SELECT * FROM events')
        res = [r for r in generateListOfDicts(query)]
        self.assertEqual(str(type(res)), "<class 'list'>")
        #
        conn.close()


if __name__ == '__main__':
    unittest.main()
