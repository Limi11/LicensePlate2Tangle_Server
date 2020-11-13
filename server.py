
# this is the http server code for communication with the things network or a raspberry pi gateway 

# **********includes*********** #

# include libraries
import json
import requests
import time
import globals


# include classes
from container import Container
from parkingmeter import ParkingMeter
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from threading import Thread, Lock

# server data
HOST_NAME = '127.0.0.1'
PORT_NUMBER = 65432

# create mutex to be threadsafe
mutex = Lock()

# at the moment we only need post since TTN sends POSTs to the server
class Server(BaseHTTPRequestHandler):
  def do_HEAD(self):
      return
  def do_POST(self):
      # response for post request
      self.send_response(200, message=None)
      # check length of post content
      content_len = int(self.headers.get('Content-Length'))
      # read content with length
      post_body = self.rfile.read(content_len)
      # decode message to utf-8 format
      spost_body = post_body.decode("utf-8")
      # json loads makes a dictionary out of json string
      jdic = json.loads(spost_body)
      # extract ID out of payload_field
      uid = jdic.get("payload_fields").get("uid")
      # lock thread during access of global container
      mutex.acquire()
      # search for parkingmeter with id
      pmobj = globals.container.get_element_by_id(uid)
      # set sensordata in parkingmeter object with id
      payload = jdic.get("payload_fields")
      pmobj.set_sensordata(payload)
      # release thread after access of global container
      mutex.release()
      return
  def do_GET(self):
      return
  def handle_http(self):
      return
  def respond(self):
      return



# this is the server function for listening to http requests
def listen():
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))




