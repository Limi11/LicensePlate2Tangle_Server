
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




def streams():

    print("Start streams thread...")

    while(True):

        # wait for event receive data
        globals.receive_data.wait()

        globals.receive_data.clear()

        id = globals.container.get_last_update_id()
        
        pm = globals.container.get_element_by_id(id)

        payload = pm.get_sensordata()


        payload = json.dumps(payload) 

        payload = "{\"iot2tangle\": [" + payload + "], " + "\"device\": \"DEVICE_ID_1\", \"timestamp\": 1558511111 }"

        payload = json.loads(payload)

        print(payload)


        # this is the payload that things network will send
        payload = { "iot2tangle": [ { "sensor": "Gyroscope", "data": [ { "x": "4514" }, { "y": "244" }, { "z": "-1830" } ] }, { "sensor": "Acoustic", "data": [ { "mp": "1" } ] } ], "device": "DEVICE_ID_1", "timestamp": 1558511111 }

        print(payload)

        client.streams_client(payload)





    