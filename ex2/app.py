from flask import Flask, request
from flask import render_template
# from giffer import Giffer


app = Flask(__name__)

##
# List Events
##############
@app.route('/api/events/', methods=['GET'])
# @app.route('/')
def listEvents():
    return 'hey1'


##
# Get Event By ID
##################
@app.route('/api/events/:id/', methods=['GET'])
# @app.route('/')
def getEventById():
    return 'hey2'


##
# Create Event
###############
@app.route('/api/events/', methods=['POST'])
def createEvent():
    # searchterms = request.form['searchterms']
    # a = Giffer(searchterms)
    # a.makeRequest()
    # a.jsonifyResult()
    # a.getGifList(50)
    # a.shuffleGifs()
    # resultloop = a.gifs_list

    return 'hey3'
