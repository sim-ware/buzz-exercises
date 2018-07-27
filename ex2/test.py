# conn = sqlite3.connect('example.db')
# c = conn.cursor()
#
#
# c.execute('''CREATE TABLE events
#          (id integer primary key, start text, end text, label text, category text)''')
#
#
# c.execute("INSERT INTO events ('start', 'end', 'label', 'category') VALUES ('2016-20-01T10:00:00Z', '2016-20-01T15:00:00Z', 'Event one', 'blue')")
# c.execute("INSERT INTO events ('start', 'end', 'label', 'category') VALUES ('2017-15-07T16:00:00Z', '2017-15-07T20:00:00Z', 'Pink Floyd', 'pink')")
# c.execute("INSERT INTO events ('start', 'end', 'label', 'category') VALUES ('2018-05-10T09:00:00Z', '2018-05-10T10:00:00Z', 'Football', 'white')")
# c.execute("INSERT INTO events ('start', 'end', 'label', 'category') VALUES ('2019-19-04T12:00:00Z', '2019-19-04T12:30:00Z', 'Meat Loaf', 'grey')")
# c.execute("INSERT INTO events ('start', 'end', 'label', 'category') VALUES ('2020-20-01T14:00:00Z', '2020-27-01T14:00:00Z', 'Chess', 'black')")
#
#
# conn.commit()
#
#
# for row in c.execute('SELECT * FROM events'):
#     print(row)
#
#
# conn.close()
