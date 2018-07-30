import unittest
import sys
sys.path.append("..")
from databaser import *
from event_exporter import *



class TestDb(unittest.TestCase):

    def test_mapEvent(self):
        db = DataBaser('test.db')
        db.getEventById(1)
        e = Event()
        e = mapEvent(db.result)
        #
        self.assertEqual(str(e.begin), '2016-08-01T10:00:00+00:00')
        self.assertEqual(str(e.name), 'blue: Event one')
        #
        db.conn.close()


    def test_exportEvent(self):
        db = DataBaser('test.db')
        db.getEventById(1)
        e = Event()
        e = mapEvent(db.result)
        #
        exportEvent(e, 'test.ics')
        with open('test.ics', 'r') as f2:
            data = f2.read()
        self.assertEqual(data[0:15], 'BEGIN:VCALENDAR')
        #
        db.conn.close()


if __name__ == '__main__':
    unittest.main()
