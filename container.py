# this is a container class to save all ParkingMeters

# imports
from parkingmeter import ParkingMeter


# class definition 
class Container(object):
    
    # the items are objects from type parkingmeter
    __items = []

    # information which object gets the latest update
    __last_update_id = ""

    # list of active reservations
    __active_reservations = []

    # add one more parking meter element to the container
    def add(self, ParkingMeter):
        self.__items.append(ParkingMeter)
        self.__active_reservations.append(False)

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
           # print(self.__items[i].get_id() + "==" + ID)
            if self.__items[i].get_id() == ID:
                return self.__items[i]
    
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

    # gives the whole container back
    def get_all_elements(self):
        return self.__items

   # this method gives a list of the next bookings from all elements back
    def get_next_booking_list(self):
        x = []
        for i in range(len(self.__items)):
            y = self.__items[i].get_next_booking()
            x.append(y)
        return x

    # get list of active reservations
    def get_active_reservations(self):
        return self.__active_reservations

    # this method gives the license plates address balances
    def set_balances(self, payments):
        for i in range(len(self.__items)):
            self.__items[i].set_balance(payments[i])

    # set list of active reservations
    def set_active_reservations(self, reslist):
        self.__active_reservations = reslist
