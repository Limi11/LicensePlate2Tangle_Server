# this is the "main" file of the gateway program

# **********includes*********** #

# include libraries
import json

# include functions
import sensordata
import booking
import reservation
import qrcode

# include classes 
from parkingmeter import ParkingMeter
from container import Container
from iota import Iota
from threading import Thread

# static initialization of parkingmeters through init file
# there should ne a dynamic initialization in future

# inti a container for our parkingmeters
container = Container()

# get init file data and fill our parkingmeters container
with open("/home/milli/LicensePlate2Tangle/init.txt") as json_file:
    data = json.load(json_file)
    for p in data["ParkingMeters"]:
        parkingmeter = ParkingMeter(p["ID"],1234,0,p["Location"],booking.newaddress())
        container.add(parkingmeter)



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

# ************start************* #
sensorthread.start()
bookingthread.start()
reservationthread.start()

# ***********test************** #
container.print()