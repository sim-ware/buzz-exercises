from flask import Flask, request
from flask import render_template
from db import *


app = Flask(__name__)

#TODO: Return Dicts, JSON

##
# List Events
##############
@app.route('/api/events/', methods=['GET'])
def returnEvents():
    conn = sqlite3.connect('example.db')
    result = getEvents(conn.cursor())
    conn.close()
    return str(result)


##
# Get Event By ID
##################
@app.route('/api/events/<int:id>/', methods=['GET'])
def returnEventById(id):
    conn = sqlite3.connect('example.db')
    result = getEventById(conn.cursor(), id)
    conn.close()
    return str(result)


##
# Create Event
###############
@app.route('/api/events/<start>/<end>/<label>/<category>/', methods=['POST'])
def returnCreatedEvent(start, end, label, category):
    conn = sqlite3.connect('example.db')
    result = createEvent(conn.cursor(), start, end, label, category)
    # conn.commit()
    conn.close()
    return str(result)
