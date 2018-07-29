from ics import Calendar, Event


def mapEvent(result):
    e = Event()
    e.name = result[0]['category'] + ": " + result[0]['label']
    e.begin = result[0]['start']
    e.end = result[0]['end']
    e.uid = result[0]['id']
    return e

def exportEvent(event):
    with open('event.ics', 'w') as my_file:
        my_file.write('BEGIN:VCALENDAR\n')
        my_file.write(str(event))
        my_file.write('\nEND:VCALENDAR')
