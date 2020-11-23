


# this is the http server code for communication with the things network or a raspberry pi gateway 

# **********includes*********** #

# include libraries
import json
import requests
import time
import globals
import base64


# include classes
from container import Container
from parkingmeter import ParkingMeter
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from threading import Thread, Lock, Event
from urllib.parse import urlparse
from iota import Address

# server data
HOST_NAME = '0.0.0.0'
PORT_NUMBER = 65432

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

      # copie content into parking meter object
      post_to_object(post_body)

      print(post_body)

      # set event for receiving data
      globals.receive_data.set()

      # we need this function to confirm that the request was successful 
      self.end_headers

      return

  def do_GET(self):

      self.send_response(200)

      # check length of post content
      #query = urlparse(self.path).query
      #query_components = dict(qc.split("=") for qc in query.split("&"))
      #uid = query_components["uid"]
      b = self.headers
      # a = self.path_headers()
      a = self.path
      self.end_headers()
      print(a)
      print(b)
      #print(uid)

      # search object with udi
      pm = globals.container.get_element_by_id("E24F43FFFE44C3FC")

      # get iota address of uid
      address = pm.get_address()

      address_with_checksum = address.with_valid_checksum()

      address_with_checksum = str(address_with_checksum)

      #self.send_header("Content-type", "text")

      #self.end_headers()

      x = {"Adr":address_with_checksum,"Tim":300}

      self.wfile.write(str(x).encode())
      
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


# this function reads the data from post request into our license plate objekt
# some steps will be outsourced in mehtods of class parkingmeter in future !
def post_to_object(data):
    # decode message to utf-8 format
      spost_body = data.decode("utf-8")

      # json loads makes a dictionary out of json string
      jdic = json.loads(spost_body)

      # extract payload out of data
      payload = jdic.get("payload_raw")

      # decode payload from base64 format
      decoded_payload = base64.b64decode(payload)
      
      # decode message to utf-8 format
      decoded_payload = decoded_payload.decode("utf-8")

      print(decoded_payload)

      # json loads makes a dictionary out of json string
      decoded_payload = json.loads(decoded_payload)

      # lock thread during access of global container
      globals.mutex.acquire()

      # extract ID out of payload_field
      uid = jdic.get("hardware_serial")

      # extract "downlink_url"
      downlink = jdic.get("downlink_url") 

      # get timestamp of sensordata
      #timestamp = jdic.get("metadata").get("time")
      timestamp="2020-11-23T23:13:26Z"

      # search for parkingmeter with id
      pmobj = globals.container.get_element_by_id(uid)

      # set sensordata in parkingmeter object with id
      pmobj.set_sensordata(decoded_payload)

      # set ttnurl 
      pmobj.set_downlink(downlink)

      # convert into unix timestemp and set timestamp in parkinmeter wiht id  
      pmobj.set_unixtimestamp(timestamp)

      # release thread after access of global container
      globals.mutex.release()



