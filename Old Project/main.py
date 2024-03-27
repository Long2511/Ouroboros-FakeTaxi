from counterfit_connection import CounterFitConnection
from counterfit_shims_grove import *
import time
import counterfit_shims_serial
import pynmea2
from flask import Flask, jsonify
from flask_cors import CORS
from threading import Thread

app = Flask(__name__)
CORS(app)


# Connect to the CounterFit virtual IoT device app
CounterFitConnection.init('127.0.0.1', 5000)


serial = counterfit_shims_serial.Serial('/dev/ttyAMA0')

@app.route('/gps')

def gps():
    return jsonify({'latitude': latitude, 'longitude': longitude})

def run_flask():
    app.run(host='localhost:8888')

Thread(target=run_flask).start()
 
def print_gps_data(line):
    print(line.rstrip())

def parse_nmea_string(nmea_string):
    msg = pynmea2.parse(nmea_string)

    return msg.latitude, msg.longitude

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


while True:
    line = serial.readline().decode('utf-8')
    latitude, longitude = parse_nmea_string(line)
    if len(line) > 0:
        print(repr(latitude) +  ", " + repr(longitude))
    time.sleep(1)
