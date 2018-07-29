import unittest
from db import *



class TestDb(unittest.TestCase):
    """
    Our basic test class
    """

    def test_getEvents(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        conn = sqlite3.connect('example.db')
        #
        res = getEvents(conn.cursor())
        self.assertEqual(len(res), 5)
        #
        conn.close()


    def test_getEventById(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        conn = sqlite3.connect('example.db')
        #
        res_one = (getEventById(conn.cursor(), 1))[0]['id']
        res_two = (getEventById(conn.cursor(), 3))[0]['id']
        res_three = (getEventById(conn.cursor(), 5))[0]['id']
        self.assertEqual(res_one, 1)
        self.assertEqual(res_two, 3)
        self.assertEqual(res_three, 5)
        #
        conn.close()


    def test_createEvent(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        conn = sqlite3.connect('example.db')
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
        conn = sqlite3.connect('example.db')
        #
        start = '2017-06-01T08:00:00Z'
        end = '2017-06-01T16:00:00Z'
        label = 'Comedy'
        category = 'black'
        res_one = createEvent(conn.cursor(), start, end, label, category)
        # conn.commit()
        # res_one = (getEventById(conn.cursor(), 6))[0]['id']
        res = getEvents(conn.cursor())
        print('AUASDUHASUCYBAUDBYCA')
        print(res_one)
        print(res)
        removeEvent(conn.cursor(), 5)
        # conn.commit()
        print(res)
        self.assertEqual(len(res), 5)


    def test_generateDict(self):
        pass


if __name__ == '__main__':
    unittest.main()
