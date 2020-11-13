# this is a container class to save all ParkingMeters

# imports
from parkingmeter import ParkingMeter


# class definition 
class Container(object):
    
    __items = []

    # add one more parking meter element to the container
    def add(self, ParkingMeter):
        self.__items.append(ParkingMeter)

    # get an parkingmeter object by ID number
    def get_element_by_id(self, ID):
        for i in range(len(self.__items)):
            if self.__items[i].get_id() == ID:
                return self.__items[i]
        return "ID is not registered!"

   



    
