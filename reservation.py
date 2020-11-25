
# this function checks if it is time for a reservation of the parking lot and
# sends the information to the parking plate 

# **********includes*********** #

# include libraries
import time
import json
import client
import globals

#include classes 
from container import Container
from parkingmeter import ParkingMeter

# **********functions*********** #

def reservation():
    print("start reservation thread...")

    while(True):
        
        # temporary list
        x = []

        # lock thread during access of global container
        globals.mutex.acquire()

        # check if there are active reservations
        for i in globals.container.get_all_elements():
            x.append(i.check_booking())
        
        # check if there was an update
        if x != globals.container.get_active_reservations():
            globals.container.set_active_reservations(x)
            for i in range(globals.container.get_container_size):
                if x[i] == True:
                    uid = globals.container.get_element_by_index(i).get_id()
                    lic = globals.container.get_element_by_index(i).get_license()
                    ts = globals.container.get_element_by_index(i).get_next_booking_start()
                    url = globals.container.get_element_by_index(i).get_url()
                    # We have an active reservation send to TTN!
                    client.ttn_client(uid,lic,ts,url)
            globals.container.set_active_reservations(x)

        # release thread after access of global container
        globals.mutex.release()
