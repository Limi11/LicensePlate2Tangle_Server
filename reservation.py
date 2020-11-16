
# this function checks if it is time for a reservation of the parking lot and
# sends the information to the parking plate 


# include libraries
import time
import json
import client
import globals

#include classes 
from container import Container
from parkingmeter import ParkingMeter


def reservation():
    print("start reservation thread...")

    #while(True):

        # TTN communication test:
        # client.ttn_client("test","https://integrations.thethingsnetwork.org/ttn-eu/api/v2/down/private_parking_meter/request_bin?key=ttn-account-v2.5FoVG4v605fZEwpptKoKXjR9frXaVlVsjjxI9HJ2cMA")
        # time.sleep(30)