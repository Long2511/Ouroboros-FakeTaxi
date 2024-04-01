import json
from counterfit_connection import CounterFitConnection
import time
import counterfit_shims_serial
import pynmea2
from flask import jsonify
from azure.iot.device import IoTHubDeviceClient, Message


# Connect to the CounterFit virtual IoT device app
CounterFitConnection.init('127.0.0.1', 5000)
serial = counterfit_shims_serial.Serial('/dev/ttyAMA0')

CONNECTION_STRING = "HostName=Oroboros.azure-devices.net;DeviceId=virtual-gps-device;SharedAccessKey=iqwrIzkhn2onCEgEYFak/s+IMnSscR9W1AIoTKiACFw="
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def gps():
    return jsonify({'latitude': latitude, 'longitude': longitude})


def print_gps_data(data):
    print(data.rstrip())


def parse_nmea_string(nmea_string):
    nmea_string = nmea_string.strip("'")
    msg = pynmea2.parse(nmea_string, check=False)

    return msg.latitude, msg.longitude


while True:
    line = serial.readline().decode('utf-8')
    latitude, longitude = parse_nmea_string(line)
    if len(line) > 0:

        gps_data = {
              "gps": { 
                  "lat": latitude,
                  "lon": longitude
                }
            }
        
        print(gps_data)

        gps_data_json = json.dumps(gps_data)

        client.send_message(gps_data_json)

    time.sleep(5)
