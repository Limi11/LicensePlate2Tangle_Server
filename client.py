# This is the http client for answering the TTN network and sending data to the STREAMS gateway

# **********includes*********** #

# include libraries
import requests
import json
import os
import base64


# include classes


# **********functions*********** #

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

    # this is the a raw payload example that things network will accept
    payload = {
    "dev_id": "parking_meter_cc1",    # The device ID
    "port": 1,                # LoRaWAN FPort
    "confirmed": False,       # Whether the downlink should be confirmed by the device
    "payload_raw": "AQIDBA=="} # Base64 encoded payload: [0x01, 0x02, 0x03, 0x04]

    # transform dict into a byte format
    payload = json.dumps(payload).encode('utf-8')

    print(payload)
    encoded_payload = payload

    # base64 is not accepted !!!
    # encoded payload from base64 format
    #encoded_payload = base64.b64encode(payload)

    # make a post request to the gateway
    r = requests.post(url_streams, data=encoded_payload, headers=headers)

    # post status of post request
    print(r.status_code)

    # we need some error handling here !
