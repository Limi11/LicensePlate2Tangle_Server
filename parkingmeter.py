# this is the parkingmeter class wich defines digital twins of the physical parking meters

import time 
import os

class ParkingMeter(object):

    __id = ""
    __channelid = ""
    __license = ""
    __location = ""
    __iotaaddress = ""
    __ttnurl = ""
    __balance = 0
    __bookings = []

    # unix timestamp of sensordata
    __timestamp = 0

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
        sdata = "[ { \"sensor\": \"Temperature\", \"data\": [{ \"temp\": \"" + str(self.__temp) + "\"}]}, { \"sensor\": \"Humidity\", \"data\": [{ \"hum\": \"" + str(self.__hum) + "\"}]}, { \"sensor\": \"Pressure\", \"data\": [{ \"pres\": \"" +  str(self.__pres) + "\"}]}, { \"sensor\": \"Status\", \"data\": [{ \"stat\": \"" + str(self.__stat) + "\"}]}]"
        return sdata

    # get timestamp of sensordata 
    def get_unixtimestamp(self):
        return self.__timestamp

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

    # method to set unix timestamp of sensordata
    def set_unixtimestamp(self, data):
        os.environ["TZ"] = "Germany/Berlin"
        time.tzset()
        #1970-01-01T00:00:00Z
        the_time = time.strptime(data,"%Y-%m-%dT%H:%M:%SZ")
        time.strftime("%Y-%m-%d %H:%M:%S %Z %z", the_time) 
        time.mktime(the_time)
        self.__timestamp = the_time
        print(the_time)

    # method to set downlink url of tth
    def set_downlink(self,ttnurl):
        self.__ttnurl = ttnurl 

    # method to set iota address
    def set_iota_address(self, address):
        self.__iotaaddress = address

    # method to set balance of iota address
    def set_balance(self, balance):
        self.__balance = balance

    # set a new booking with license number start and endtime 
    def set_booking(self, data):
        # parkdauer berechnen aktuell statisch 10Miota/h
        seconds = self.__balance/1000000*60*60
        # get license out of data
        license = data.get("lic")
        # get stime out of data
        stime = data.get("ts")
        # calculate endtime stime unixtime + seconds
        etime = data.get("") + seconds
        self.__bookings.append({"lic":license,"ts":stime,"te":etime})
        print("New booking:" + str(self.__bookings[-1]))


    def delete_booking(self):
        print("delete bookings")

    def set_payment(self):
        print("set payment")

    def parking_json(self):
        print("give sensor data as json back")

    def sensor_json(self):
        print("give parking data as json back")

    def get_address(self):
        return self.__iotaaddress

    def print(self):
        print(self.__id)
        print(self.__channelid) 
        print(self.__iotaaddress)

    


