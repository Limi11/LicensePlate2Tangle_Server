
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

        time.sleep(10)

        # temporary list
        x = []

        # lock thread during access of global container
        globals.mutex.acquire()

        # check if there are active reservations
        for i in globals.container.get_all_elements():
            #print("Check element: " + str(i))
            #print("ID of element: " + str(i.get_id()))
            x.append(i.check_booking())

        #print("List of elements with reservation: " + str(x))

        # check if there was an update
        #if x != globals.container.get_active_reservations():
        for i in range(len(x)):
             #print("Index of checking loop: " + str(i))
             if x[i] == True:
                 uid = globals.container.get_element_by_index(i).get_id()
                 lic = globals.container.get_element_by_index(i).get_license()
                 ts = globals.container.get_element_by_index(i).get_next_booking_start()
                 url = globals.container.get_element_by_index(i).get_url()
                 #print(str(uid) + str(lic) + str(ts) + str(url))
                 # We have an active reservation send to TTN!
                 print("Send booking Information to TTN")
                 client.ttn_client(uid,lic,ts,url)
       
        #globals.container.set_active_reservations(x)

        # release thread after access of global container
        globals.mutex.release()
