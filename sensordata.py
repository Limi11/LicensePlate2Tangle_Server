
# this function is listening for sensor data 

# json read full raw body format see: https://www.thethingsnetwork.org/docs/applications/http/ 
# json read payload: {"s":0xFF,"t":23,"h":70,"p":1000}}
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

          