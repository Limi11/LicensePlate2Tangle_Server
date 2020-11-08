# this is a container class to save all ParkingMeters

# imports
from parkingmeter import ParkingMeter

# class definition 
class Container(object):
    
    __items = []

    def add(self, ParkingMeter):
        self.__items.append(ParkingMeter)

    def print(self):
        for p in self.__items:
            p.print()

   



    
