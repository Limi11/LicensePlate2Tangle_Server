
# this is the "main" file of the gateway program

# **********includes*********** #

# include libraries
import json

# include functions
import booking
import reservation
import qrcode
import streams
import sensordata
import globals
import subprocess


# include classes 
from parkingmeter import ParkingMeter
from container import Container
from iota import Iota
from threading import Thread

# ********initialization********* #

# static initialization of parkingmeters through init file
# there should ne a dynamic initialization in future
# inti a container for our parkingmeters
# we need the container global, therefore we initialize it in a function

globals.container_init()
globals.event_init()
globals.addrees_index_init()
globals.mutex()

# get init file data and build our parkingmeters container
with open("/home/ubuntu/IOTLicensePlate2Tangle/LicensePlate2Tangle_Server/init.txt") as json_file:
    data = json.load(json_file)
    for p in data["ParkingMeters"]:
        parkingmeter = ParkingMeter(p["ID"],1234,"Free",p["Location"],booking.newaddress())
        globals.container.add(parkingmeter)

# now we need to get the reservation informations back from tangle
# ... this will be done with keepy in future

# the keepy and streams-http-gateway folders must be in the project folder!
# start http streams gateway
subprocess.call("gnome-terminal --command=\"cargo run --release\"" , cwd="Streams-http-gateway", shell=True)
# start keepy 
subprocess.call("gnome-terminal --command=\"node keepy.js\"" , cwd="Keepy", shell=True)

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

# ***********test************** #
