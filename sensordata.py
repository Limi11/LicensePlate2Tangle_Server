
# this function is listening for sensor data 
# socket communication see https://realpython.com/python-sockets/

# json read full raw body format see: https://www.thethingsnetwork.org/docs/applications/http/ 
# json read payload: {"uid:"PM1","stat":0xFF,"sens":{"temp":23,"hum":70,"pres":1000,"acc":2000,"occ":0}}
# json send format: {"cmd":0xFF,"lic":"LB-AB-1234","qr":"2g 3d f2 ..."}


# **********includes*********** #

# include libraries
import time
import json

# include classes
from http.server import HTTPServer
from server import Server

# server data
HOST_NAME = '127.0.0.1'
PORT_NUMBER = 65432

# sensordata function is a thread in gateway.py
def sensordata():
    print("start sensordata")
    while True:
            httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
            print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                pass
            httpd.server_close()
            print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))