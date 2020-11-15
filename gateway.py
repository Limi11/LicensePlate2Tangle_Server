
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

# get init file data and build our parkingmeters container
with open("/home/milli/LicensePlate2Tangle/init.txt") as json_file:
    data = json.load(json_file)
    for p in data["ParkingMeters"]:
        parkingmeter = ParkingMeter(p["ID"],1234,"Free",p["Location"],booking.newaddress())
        globals.container.add(parkingmeter)

# now we need to get the reservation informations back from tangle

# start streams gateway read back channel ID and save information into init.txt
# ...


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
