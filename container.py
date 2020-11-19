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
    
    # return the id of license plate that gets the last update
    def get_last_update_id(self):
        return self.__last_update_id

    # this function gives a list of all used iota adresses back
    def get_iota_adress_list(self):
        addresses = []
        for i in range(len(self.__items)):
            # get parkingmeter object
            licenseplate = self.get_element_by_index(i)
            # get iota address of parkingmeter
            address = licenseplate.get_address()
            addresses.append(address)
        return addresses

    def get_all_elements(self):
        return self.__items

    # this method gives the license plates address balances
    def set_balances(self, payments):
        for i in range(len(self.__items)):
            self.__items[i].set_balance(payments[i])

   



    
