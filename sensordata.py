
# this function is listening for sensor data 

# json read full raw body format see: https://www.thethingsnetwork.org/docs/applications/http/ 
# json read payload: {"uid:"PM1","stat":0xFF,"sens":{"temp":23,"hum":70,"pres":1000,"acc":2000,"occ":0}}
# json send format: {"cmd":0xFF,"lic":"LB-AB-1234","qr":"2g 3d f2 ..."}


# **********includes*********** #

# include libraries
import time
import json
import server

# include classes


# sensordata function is a thread in gateway.py
def sensordata():
    print("Start sensordata thread...")
    while True:
        ## start listening for data
        server.listen()

          