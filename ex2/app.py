from flask import Flask, request
from flask import render_template
from flask import jsonify
from flask import send_file
from db import *
import json


app = Flask(__name__)


##
# List Events
##############
@app.route('/api/events/', methods=['GET'])
def returnEvents():
    conn = sqlite3.connect('example.db')
    result = getEvents(conn.cursor())
    conn.close()
    return jsonify({'result':result})


##
# Get Event By ID
##################
@app.route('/api/events/<int:id>/', methods=['GET'])
def returnEventById(id):
    conn = sqlite3.connect('example.db')
    result = getEventById(conn.cursor(), id)
    conn.close()
    return jsonify({'result':result})


##
# Create Event
###############
@app.route('/api/events/<string:start>/<string:end>/<string:label>/<string:category>/', methods=['POST'])
def returnCreatedEvent(start, end, label, category):
    conn = sqlite3.connect('example.db')
    result = createEvent(conn.cursor(), start, end, label, category)
    # conn.commit()
    conn.close()
    return jsonify({'result':result})


##
# Export Event As Attachment By ID
###################################
@app.route('/api/events/<int:id>/export/', methods=['GET'])
def exportEventById(id):
    conn = sqlite3.connect('example.db')
    result = getEventById(conn.cursor(), id)
    conn.close()
    json_result = jsonify({'result':result})
    # return json_result
    # return 'export'
    path = 'my.ics'
    return send_file(path, as_attachment=True)
