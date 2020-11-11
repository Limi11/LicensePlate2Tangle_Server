
# **********includes*********** #

# include libraries
import json
import requests

# include classes
from http.server import BaseHTTPRequestHandler

# at the moment we only need post since TTN sends POSTs to the server

class Server(BaseHTTPRequestHandler):
  def do_HEAD(self):
      return
  def do_POST(self):
      content_len = int(self.headers.get('Content-Length'))
      post_body = self.rfile.read(content_len)
      spost_body = post_body.decode("utf-8")
      # json loads makes a dictionary out of json string
      jdic = json.loads(spost_body)
      x = jdic.get("iot2tangle")
      x = x[1]
      print(x)
      print(type(jdic))
      print(jdic)
      print(type(x))
      return
  def do_GET(self):
      return
  def handle_http(self):
      return
  def respond(self):
      return







