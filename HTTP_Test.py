
# This is a testscript for simulation of the Things Netwok http post messages

# **********includes*********** #

# include libraries
import requests
import json
import os
import client
import globals


# include classes
from container import Container


# ********initialization********* #

# 127.0.0.1 is the local host address, this is staticaly defined because thats only a testscript!
urlapp = "http://127.0.0.1:65432/uid:E24F43FFFE44C3FC"
urlttn = "http://127.0.0.1:65432"

# definition of headers type
headers = {'content-type': 'application/json', 'Accept': 'text/plain'}

# this is the payload that things network will send
payload = {
  "app_id": "my-app-id",
  "dev_id": "E24F43FFFE44C3FC",
  "hardware_serial": "E24F43FFFE44C3FC",
  "port": 1,
  "counter": 2,

  "is_retry": False,
  "confirmed": False,
  "payload_raw": "eyJoIjo1Ni4yOSwidCI6MjEuNzAsInAiOjk4MS40NiwicyI6IjB4MDAifQ==",
  "payload_fields": {},
  "metadata": {
    "time": "2020-11-24T21:16:28.425589977Z",
    "frequency": 868.1,
    "modulation": "LORA",
    "data_rate": "SF7BW125",
    "bit_rate": 50000,
    "coding_rate": "4/5",
    "gateways": [
      {
        "gtw_id": "ttn-herengracht-ams",
        "timestamp": 12345,
        "time": "1970-01-01T00:00:00Z",
        "channel": 0,
        "rssi": -25,
        "snr": 5,
        "rf_chain": 0,
        "latitude": 52.1234,
        "longitude": 6.1234,
        "altitude": 6 
      },
    ],
    "latitude": 52.2345,
    "longitude": 6.2345,
    "altitude": 2
  },
  "downlink_url": "https://integrations.thethingsnetwork.org/ttn-eu/api/v2/down/my-app-id/my-process-id?key=ttn-account-v2.secret"
}


# ********functions********* #

# convert from dictionary to string
payload = json.dumps(payload)

# make a post request to the gateway
r = requests.post(urlttn, data=payload, headers=headers)

# make a get request to the gateway
# old format  params={"uid":"E24F43FFFE44C3FC"}
#r = requests.get(urlapp)

# post status of post request
# text = r.text.decode("tf-8")
#print(r.text)

#print(r)

