# this is a container class to save all ParkingMeters

# imports
from parkingmeter import ParkingMeter


# class definition 
class Container(object):
    
    # the items are objects from type parkingmeter
    __items = []

    # information which object gets the latest update
    __last_update_id = ""

    # add one more parking meter element to the container
    def add(self, ParkingMeter):
        self.__items.append(ParkingMeter)

    # get number of parkinmeters
    def get_container_size(self):
        size = len(self.__items)
        return size
    
    # get an parkinmeter by index
    def get_element_by_index(self, index):
        return self.__items[index]  

    # get an parkingmeter object by ID number
    def get_element_by_id(self, ID):
        self.__last_update_id = ID
        for i in range(len(self.__items)):
            if self.__items[i].get_id() == ID:
                return self.__items[i]
        return "ID is not registered!"
    
    def get_last_update_id(self):
        return self.__last_update_id

    def get_all_elements(self):
        return self.__items

   



    
