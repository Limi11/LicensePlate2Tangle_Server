
# this is the "main" file of the gateway program

# **********includes*********** #

# include libraries
import json

# include functions
import booking
import reservation
import streams
import sensordata
import globals
import subprocess
import pathlib
import time
import client
import os

# include classes 
from parkingmeter import ParkingMeter
from container import Container
from iota import Iota
from threading import Thread
from wallet import Wallet


# ********initialization********* #

# static initialization of parkingmeters through init file
# there should ne a dynamic initialization in future
# inti a container for our parkingmeters
# we need the container global, therefore we initialize it in a function

globals.container_init()
globals.event_init()
globals.addrees_index_init()
globals.mutex()
globals.hostip()
globals.port()

# get the current working directory
path = str(pathlib.Path(__file__).parent)
#print(path)

# get init file data and build our parkingmeters container #home/ubuntu
with open(path + "/init.txt") as json_file:
    data = json.load(json_file)
    for p in data["ParkingMeters"]:
        parkingmeter = ParkingMeter(p["ID"],1234,"Free",p["Location"],booking.newaddress())
        globals.container.add(parkingmeter)
    globals.hostip = data["HOST"]
    globals.port = int(data["PORT"])
    seed = str(data["SEED"])
    autorun = bool(data["Auto_Run_Gateway"])
    

# now we need to get the reservation informations back from tangle
# ... this will be done with keepy in future ..............


# the keepy and streams-http-gateway folders must be in the project folder!
# start http streams gateway & start keepy
DEVNULL = open(os.devnull, 'wb')
if(autorun == True):
    subprocess.call("gnome-terminal --command=\"cargo run --release\"" , cwd="Streams-http-gateway", shell=True, stdout=DEVNULL, stderr=DEVNULL)
    subprocess.call("gnome-terminal --command=\"node keepy.js\"" , cwd="Keepy", shell=True, stdout=DEVNULL, stderr=DEVNULL )
else:
    print("You need to start Keepy and HTTP Gateway manualy!")

# **********functions*********** #
# here only short functions are defined
# bigger functions are defined in other files


# ***********threads************* #

# this is the thread for the sensordata() function
sensorthread = Thread(target=sensordata.sensordata)
# this is the thread for the booking() function
bookingthread = Thread(target=booking.booking)
# this is the thread for the reservation() function
reservationthread = Thread(target=reservation.reservation)
# this is the thread that sends parking meters data to IOTA Streams
streamsthread = Thread(target=streams.streams)

# ************start************* #
sensorthread.start()
bookingthread.start()
reservationthread.start()
streamsthread.start()

print("Listening on port: " + str(globals.port)) 

# ***********test************** #


#time.sleep(10)
#uid = globals.container.get_element_by_index(0).get_id()
#lic = globals.container.get_element_by_index(0).get_license()
#ts = globals.container.get_element_by_index(0).get_next_booking_start()
#client.ttn_client(uid,lic,ts,"https://integrations.thethingsnetwork.org/ttn-eu/api/v2/down/my-app-id/my-process-id?key=ttn-account-v2.secret")
