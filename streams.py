
# this is the thread function that sends periodically (every 10 s) streams data to the iota tangele
 

# **********includes*********** #

# include libraries
import time
import json
import client
import globals

#include classes 
from container import Container
from parkingmeter import ParkingMeter


# this is an example payload for the streams gateway
# payload = { "iot2tangle": [ { "sensor": "Gyroscope", "data": [ { "x": "4514" }, { "y": "244" }, { "z": "-1830" } ] }, { "sensor": "Acoustic", "data": [ { "mp": "1" } ] } ], "device": "DEVICE_ID_1", "timestamp": 1558511111 }


def streams():

    print("Start streams thread...")

    while(True):

        # wait for event receive data
        globals.receive_data.wait()
        
        # get id of device that sends the new data
        id = globals.container.get_last_update_id()
        
        # get object that sends data 
        pm = globals.container.get_element_by_id(id)

        # get sensordata as json string
        data = pm.get_streamsdata()

        # get timestemp from sensordata
        timestamp = pm.get_unixtimestamp()

        # get device id
        devid = pm.get_id()

        # build 
        payload = "{\"iot2tangle\": [" + data + "] ," + "\"device\": \"" + str(devid) + "\", \"timestamp\": \"" + str(timestamp) + "\" }"

        print(payload)

        # string to json conerstion
        payload = json.loads(payload)

        print(payload)

        client.streams_client(payload)

        # clear receive data event, waiting for new receive data event
        globals.receive_data.clear()





    