
# this is the thread function 
 

# **********includes*********** #

# include libraries
import time
import json
import client
import globals

#include classes 
from container import Container
from parkingmeter import ParkingMeter
from threading import Thread, Lock, Event


# this is an example payload for the streams gateway
# payload = { "iot2tangle": [ { "sensor": "Gyroscope", "data": [ { "x": "4514" }, { "y": "244" }, { "z": "-1830" } ] }, { "sensor": "Acoustic", "data": [ { "mp": "1" } ] } ], "device": "DEVICE_ID_1", "timestamp": 1558511111 }


# ********functions********* #

def streams():

    print("Start streams thread...")

    while(True):

        # wait for event receive data
        globals.receive_data.wait()
        
        # lock thread during access of global container
        globals.mutex.acquire()

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

        # release thread after access of global container
        globals.mutex.release()

        # build 
        # '{ "iot2tangle": [ { "sensor": "Temperature", "data": [ { "temp": "21.7" } ] }, { "sensor": "Humidity", "data": [ { "hum": "56.29"}]}, { "sensor": "Pressure", "data": [ { "pres": "981.46" } ] }, { "sensor": "Status", "data": [ {"stat": "0x00" } ] }, { "sensor": "Bookings", "data": [ { "book": "2" } ] }, { "sensor": "Address", "data": [ { "addr": "IEEUHAEC9M9KGQWVA9BBYI9MFTJFDYOYKCYCH9CATDMUJLSMUJYH9AXQKTYLYNMIHAFVR9L9OBRXRODB9" } ] } ], "device": "E24F43FFFE44C3FC", "timestamp": "1606202006" }'

        payload = "{\"iot2tangle\": " + data + " ," + "\"device\": \"" + str(devid) + "\", \"timestamp\": \"" + str(timestamp) + "\" }"
        print(payload)

        # string to json conerstion
        payload = json.loads(payload)

        print(payload)

        client.streams_client(payload)

        # clear receive data event, waiting for new receive data event
        globals.receive_data.clear()





    