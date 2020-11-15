# this is the parkingmeter class wich defines digital twins of the physical parking meters


class ParkingMeter(object):

    __id = ""
    __channelid = ""
    __license = ""
    __location = ""
    __iotaaddress = ""

    __temp = 0.0
    __hum = 0
    __pres = 0
    __acc = 0
    __occ = 0
    __data = {}

    # consturctor 
    def __init__(self,id,channelid,license,location,iotaaddress):
        self.__id = id
        self.__channelid = channelid
        self.__license = license
        self.__location = location
        self.__iotaaddress = iotaaddress
    
    # method to get id of parking meter
    def get_id(self):
        return str(self.__id) 

    # method to print sensordata in json format
    def get_sensordata(self):
        return self.__data

    # method to set sensor values out http post sensor dict
    def set_sensordata(self,data):
        self.__data = data
        self.__temp = data.get("temp")
        self.__hum = data.get("hum")
        self.__pres = data.get("pres")
        self.__acc = data.get("acc")
        self.__occ = data.get("occ")

    
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

    


