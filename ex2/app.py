from flask import Flask, request
from flask import render_template
from flask import jsonify
from flask import send_file
from databaser import *
from event_exporter import *



app = Flask(__name__)


##
# List Events
##############
@app.route('/api/events/', methods=['GET'])
def returnEvents():
    db = DataBaser('example.db')
    db.getEvents()
    db.conn.close()
    return jsonify({'result':db.result})


##
# Get Event By ID
##################
@app.route('/api/events/<int:id>/', methods=['GET'])
def returnEventById(id):
    db = DataBaser('example.db')
    db.getEventById(id)
    db.conn.close()
    return jsonify({'result':db.result})


##
# Create Event
###############
@app.route('/api/events/<string:start>/<string:end>/<string:label>/<string:category>/', methods=['POST'])
def returnCreatedEvent(start, end, label, category):
    db = DataBaser('example.db')
    db.createEvent(start, end, label, category)
    e = mapEvent(db.result)
    db.conn.commit()
    db.conn.close()
    return jsonify({'result':db.result})


##
# Delete Event
###############
@app.route('/api/events/<int:id>/delete/', methods=['GET'])
def deleteEvent(id):
    db = DataBaser('example.db')
    db.removeEvent(id)
    db.conn.commit()
    db.conn.close()
    return db.result


##
# Export Event As Attachment By ID
###################################
@app.route('/api/events/<int:id>/export/', methods=['GET'])
def exportEventById(id):
    db = DataBaser('example.db')
    db.getEventById(id)
    db.conn.close()
    path = 'event.ics'
    e = mapEvent(db.result)
    exportEvent(e, path)
    return send_file(path, as_attachment=True)
