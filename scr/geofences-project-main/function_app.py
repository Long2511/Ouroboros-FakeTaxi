import azure.functions as func
import json
import logging
import os
import requests

app = func.FunctionApp()

maps_key = os.environ['MAPS_KEY']
geofence_udid = os.environ['GEOFENCE_UDID']


@app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="eventhubname",
                               connection="IOT_HUB_CONNECTION_STRING") 
def gps_trigger(azeventhub: func.EventHubEvent):
    event_data = json.loads(azeventhub.get_body().decode('utf-8'))

    lat = event_data['gps']['lat']
    lon = event_data['gps']['lon']

    url = 'https://atlas.microsoft.com/spatial/geofence/json'

    params = {
        'api-version': 1.0,
        'deviceId': 'gps-sensor',
        'subscription-key': maps_key,
        'udid' : geofence_udid,
        'lat' : lat,
        'lon' : lon
    }

    response = requests.get(url, params=params)
    response_body = json.loads(response.text)

    logging.info(response_body)

    distance = response_body['geometries'][0]['distance']
    logging.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    if distance == 999:
        logging.info('User is outside geofence')
    elif distance > 0:
        logging.info(f'User is just outside geofence by a distance of {distance}m')
    elif distance == -999:
        logging.info(f'User is inside geofence')
    else:
        logging.info(f'User is just inside geofence by a distance of {distance}m')
    logging.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')




# @app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="eventhubname",
#                                connection="IOT_HUB_CONNECTION_STRING") 
# def eventhub_trigger(azeventhub: func.EventHubEvent):
#     logging.info('Python EventHub trigger processed an event: %s',
#                 azeventhub.get_body().decode('utf-8'))
