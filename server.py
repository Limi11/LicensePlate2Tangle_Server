#  This is the http server function which can get post messagen from TTN network or get messages from mobile app

# **********includes*********** #

# include libraries
import json
import requests
import time
import base64
import globals
import html
import datetime

# include classes
from container import Container
from parkingmeter import ParkingMeter
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from threading import Thread, Lock, Event
from urllib.parse import urlparse
from iota import Address


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

      print(post_body)
      
      # copie content into parking meter object
      post_to_object(post_body)

      # set event for receiving data
      globals.receive_data.set()

      # we need this function to confirm that the request was successful 
      self.end_headers

      return

  def do_GET(self):

      self.send_response(200)

      header = self.headers
      
      header = header.as_string()

      print(header)

      # the uid is in the path
      #path = self.path
      
      self.end_headers()

      #path = str(path)

      # print(path)

      # print("Das ist der header: " + header)

      #index = header.find(":")
      #index = index + 2

      uid = header[5:21]
      
      #print("This is the header: " + str(header))
      print("New GET request from uid: " + uid)

      #print(type(uid))
      #print(uid)
      #print(str(uid))
      # search object with udi
      try:
          pm = globals.container.get_element_by_id(str(uid))
      except:
          print("Uid from GET request is not registered!")
          pass

      # get iota address of uid
      address = pm.get_address()

      # print(address)
      # android app needs an address with checksum
      address_with_checksum = address.with_valid_checksum()
      # print(address_with_checksum)
      # convert address to string
      address_with_checksum = str(address_with_checksum)

      # get next booking 
      nextbooking = pm.get_next_booking_end()

      print(nextbooking)

      # calculate allowed parking time
      parking_time = nextbooking - int(time.time())

      print(str(parking_time))

      #sdata = {"Adr":address_with_checksum,"Tim":parking_time}
      sdata = {"Adr":address_with_checksum,"Tim":"100"}


      print(sdata)

      self.wfile.write(str(sdata).encode())
      
      return

  def handle_http(self):

      return

  def respond(self):

      return


# this is the server function for listening to http requests
def listen():
    httpd = HTTPServer((globals.hostip, globals.port), Server)
    print(time.asctime(), 'Server UP - %s:%s' % (globals.hostip, globals.port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server DOWN - %s:%s' % (globals.hostip, globals.port))


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
      try:
          decoded_payload = json.loads(decoded_payload)
          # lock thread during access of global container
          globals.mutex.acquire()

          # extract ID out of payload_field
          uid = jdic.get("hardware_serial")

          # extract "downlink_url"
          downlink = jdic.get("downlink_url")
          print("New downlink url: " + str(downlink)) 

          # get timestamp of sensordata
          timestamp = jdic.get("metadata").get("time")
          index = timestamp.find(".")
          #format from TTN 2020-11-24T21:16:28.425589977Z
          #timestamp="2020-11-23T23:13:26Z"
          #timestamp cut last 11 chars and add Z to get right format
          timestamp = timestamp[:index] + "Z"

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
      except:
          print("Empty message for LORA response!")
            




