# This is the http client for answering the TTN network and sending data to the STREAMS gateway

# **********includes*********** #

# include libraries
import requests
import json
import os


# include classes



# this is the function for sending data over keepy to streams http gateway to tangle
def streams_client(data):
    
    # 127.0.0.1 is the local host address
    url_keppy = "http://127.0.0.1:3002/messages"

    # definition of headers type
    headers = {'content-type': 'application/json'}

    # convert from dictionary to string
    data = json.dumps(data)

    # make a post request to the gateway
    r = requests.post(url_keppy, data=data, headers=headers)

    # post status of post request
    print(r.status_code)

    # we need some error handling here !


# this is the funcion for sending data to the things network
def ttn_client(data, url_streams):
    
    # definition of headers type
    headers = {'content-type': 'application/json'}

    # this is the payload that things network will send
    payload = { "iot2tangle": [ { "sensor": "Gyroscope", "data": [ { "x": "4514" }, { "y": "244" }, { "z": "-1830" } ] }, { "sensor": "Acoustic", "data": [ { "mp": "1" } ] } ], "device": "DEVICE_ID_1", "timestamp": 1558511111 }


    # convert from dictionary to string
    payload = json.dumps(payload)

    # make a post request to the gateway
    r = requests.post(url_streams, data=payload, headers=headers)

    # post status of post request
    print(r.status_code)

    # we need some error handling here !
