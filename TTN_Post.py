
# This is a testscript for simulation of the Things Netwok http post messages

# include libraries
import requests
import json
import os


# include classes


# 127.0.0.1 is the local host address
url = "http://127.0.0.1:65432"

# definition of headers type
headers = {'content-type': 'application/json', 'Accept': 'text/plain'}

# this is the payload that things network will send
payload = {
  "app_id": "my-app-id",
  "dev_id": "my-dev-id",
  "hardware_serial": "0102030405060708",
  "port": 1,
  "counter": 2,
  "is_retry": False,
  "confirmed": False,
  "payload_raw": "AQIDBA==",
  "payload_fields": {
    "uid":"PM1",
    "stat":0xFF,
    "sens": [
        {
          "temp":23,
          "hum":70,
          "pres":1000,
          "acc":2000,
          "occ":0
          },
        ],
  },
  "metadata": {
    "time": "1970-01-01T00:00:00Z",
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


# convert from dictionary to string
payload = json.dumps(payload)

# make a post request to the gateway
r = requests.post(url, data=payload, headers=headers)

# post status of post request
print(r.status_code)

#print(r)