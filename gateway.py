# this is the "main" file of the gateway program

# **********includes*********** #

#include libraries
from iota import Iota
from threading import Thread

#include functions
import sensordata
import booking
import reservation
import qrcode

# include classes 
from parkingmeter import ParkingMeter
from container import Container


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

parkingmeter = ParkingMeter(0,1234,1,"GPS coordinates",booking.newaddress())
parkingmeter.get_sensordata()
parkingmeter.get_address()

container = Container(parkingmeter)
container.pop()