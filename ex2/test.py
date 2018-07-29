# import sqlite3
# conn = sqlite3.connect('example.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE events
#          (id integer primary key, start text, end text, label text, category text)''')
# c.execute("INSERT INTO events ('start', 'end', 'label', 'category') VALUES ('2016-08-01T10:00:00Z', '2016-08-01T15:00:00Z', 'Event one', 'blue')")
# c.execute("INSERT INTO events ('start', 'end', 'label', 'category') VALUES ('2017-12-07T16:00:00Z', '2017-12-07T20:00:00Z', 'Pink Floyd', 'pink')")
# c.execute("INSERT INTO events ('start', 'end', 'label', 'category') VALUES ('2018-05-10T09:00:00Z', '2018-05-10T10:00:00Z', 'Football', 'white')")
# c.execute("INSERT INTO events ('start', 'end', 'label', 'category') VALUES ('2019-05-04T12:00:00Z', '2019-05-04T12:30:00Z', 'Meat Loaf', 'grey')")
# c.execute("INSERT INTO events ('start', 'end', 'label', 'category') VALUES ('2020-11-01T14:00:00Z', '2020-11-01T19:00:00Z', 'Chess', 'black')")
# conn.commit()
# for row in c.execute('SELECT * FROM events'):
#     print(row)
# conn.close()

from ics import Calendar, Event
# c = Calendar()
e = Event()
#
#
from db import *
conn = sqlite3.connect('example.db')
result = getEventById(conn.cursor(), str(2))
conn.close()
#
#
e.name = result[0]['category'] + ": " + result[0]['label']
e.begin = result[0]['start']
e.end = result[0]['end']
e.uid = result[0]['id']
#
# c.events.add(e)
# c.events
# #
with open('my.ics', 'w') as my_file:
    my_file.write(str(e))

# Check if making the year 2018 changes things - rerun DB with all dates changed to 2018

# How to add these to the calendar?
# BEGIN:VCALENDAR
# END:VCALENDAR
