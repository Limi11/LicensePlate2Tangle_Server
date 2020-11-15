# this is the parkingmeter class wich defines digital twins of the physical parking meters


class ParkingMeter(object):

    __id = ""
    __channelid = ""
    __license = ""
    __location = ""
    __iotaaddress = ""
    __ttnurl = ""

    # temperature
    __temp = 0.0
    # humidity
    __hum = 0
    # pressure
    __pres = 0
    # status
    __stat = 0x00

    # json data from device
    __data = ""

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

    # method to return sensordata in json streams format
    def get_sensordata(self):
        sdata = "[ {\"sensor\": \"Temperature\", \"data\":" + str(self.__temp) + "}, { \"sensor\": \"Humidity\", \"data\":" + str(self.__hum) + "}, {\"sensor\": \"Pressure\", \"data\":" +  str(self.__pres) + "}, {\"information\": \"Status\", \"data\":\"" + str(self.__stat) + "\"}]"
        return sdata

    # method to get uplink url from ttn
    def get_url(self, ttnurl):
        return self.__ttnurl
  
    def get_bookings(self):
        print("get bookings")

  # method to set sensor values out http post sensor dict
    def set_sensordata(self,data):
        self.__data = data
        self.__temp = data.get("t")
        self.__hum = data.get("h")
        self.__pres = data.get("p")
        self.__stat = data.get("s")

    # method to set downlink url of tth
    def set_downlink(self,ttnurl):
        self.__ttnurl = ttnurl 


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

    


