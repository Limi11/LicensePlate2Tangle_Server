# this is a container class to save all ParkingMeters

# imports
from parkingmeter import ParkingMeter

# class definition 
class Container(object):
    
    __items = []

    def __init__(self, ParkingMeter):
        self.__items.append(ParkingMeter)

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()



    
