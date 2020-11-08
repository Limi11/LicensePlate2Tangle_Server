# this is the parkingmeter class wich defines digital twins of the physical parking meters


class ParkingMeter(object):

    def __init__(self,id,channelid,occupation,location,iotaaddress):
        self.__id = id
        self.__channelid = channelid
        self.__occupation = occupation
        self.__location = location
        self.__iotaaddress = iotaaddress
    
    def get_sensordata(self):
        print("get sensordata")

    def set_sensordata(self):
        print("set sensordata")

    def get_bookings(self):
        print("get bookings")

    def set_bookings(self):
        print("set bookings")

    def delete_booking(self):
        print("delete bookings")

    def set_payment(self):
        print("set payment")

    def parking_json(self):
        print("give sensor data as json back")

    def sensor_json(self):
        print("give parking data as json back")

    def get_address(self):
        print(self.__iotaaddress)

    def print(self):
        print(self.__id)
        print(self.__channelid) 
        print(self.__iotaaddress)


