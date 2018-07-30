import unittest
import sys
sys.path.append("..")
from databaser import *
from event_exporter import *



class TestDb(unittest.TestCase):

    def test_mapEvent(self):
        conn = sqlite3.connect('test.db')
        res = getEventById(conn.cursor(), 1)
        e = Event()
        e = mapEvent(res)
        #
        self.assertEqual(str(e.begin), '2016-08-01T10:00:00+00:00')
        self.assertEqual(str(e.name), 'blue: Event one')
        #
        conn.close()


    def test_exportEvent(self):
        conn = sqlite3.connect('test.db')
        res = getEventById(conn.cursor(), 1)
        e = Event()
        e = mapEvent(res)
        #
        exportEvent(e, 'test.ics')
        with open('test.ics', 'r') as f2:
            data = f2.read()
        self.assertEqual(data[0:15], 'BEGIN:VCALENDAR')
        #
        conn.close()


if __name__ == '__main__':
    unittest.main()
