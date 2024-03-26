from counterfit_connection import CounterFitConnection
from counterfit_shims_grove import *
import time
import counterfit_shims_serial
import pynmea2


# Connect to the CounterFit virtual IoT device app
CounterFitConnection.init('127.0.0.1', 5000)


serial = counterfit_shims_serial.Serial('/dev/ttyAMA0')

def print_gps_data(line):
    print(line.rstrip())

def parse_nmea_string(nmea_string):
    msg = pynmea2.parse(nmea_string)

    return msg.latitude, msg.longitude



while True:
    line = serial.readline().decode('utf-8')
    latitude, longitude = parse_nmea_string(line)
    if len(line) > 0:
        print(repr(latitude) +  ", " + repr(longitude))


    time.sleep(1)
