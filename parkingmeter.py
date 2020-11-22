# this is the parkingmeter class wich defines digital twins of the physical parking meters

# **********includes*********** #

# include libraries
import time 
import datetime
import os
import json

class ParkingMeter(object):

    __id = ""
    __channelid = ""
    __license = ""
    __location = ""
    __iotaaddress = ""
    __ttnurl = ""
    __balance = 0
    __bookings = []
    __nextbooking = {'lic':'', 'ts': 0, 'te': 0}
    __reserved = False
    __occupied = False

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

    # data for streams
    __sdata = [{ "sensor": "Temperature", 
    "data": [{ "temp": ""}]}, { "sensor": "Humidity", 
    "data": [{ "hum": ""}]}, { "sensor": "Pressure", 
    "data": [{"pres":""}]}, { "sensor": "Status", 
    "data": [{ "stat": ""}]},{ "sensor": "Bookings", 
    "data": [{ "book": []}]} ]
    
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
    def get_streamsdata(self):
        self.__sdata[0]["data"][0]["temp"] = str(self.__temp)
        self.__sdata[0]["data"][0]["hum"] = str(self.__hum)
        self.__sdata[0]["data"][0]["pres"] = str(self.__pres)
        self.__sdata[0]["data"][0]["stat"] = str(self.__stat)
        self.__sdata[0]["data"][0]["book"] = str(self.__bookings)
        x = json.dumps(self.__sdata[0])
        return x

    # get timestamp of sensordata 
    def get_unixtimestamp(self):
        return self.__timestamp

    # method to get uplink url from ttn
    def get_url(self):
        return self.__ttnurl

    # set the next booking time
    def get_next_booking(self):
        return self.__nextbooking

    # get iota address
    def get_address(self):
        return self.__iotaaddress
    
    # set the next booking time
    def set_next_booking(self):
        x = self.__bookings[0]["ts"]
        for i in range(len(self.__bookings)-1):
            if x < self.__bookings[i+1]["ts"]:
                x = self.__bookings[i+1]
        self.__nextbooking = x

    # method to set sensor values out http post sensor dict
    def set_sensordata(self,data):
        self.__data = data
        self.__temp = data.get("t")
        self.__hum = data.get("h")
        self.__pres = data.get("p")
        self.__stat = data.get("s")

    # method to set unix timestamp of sensordata
    def set_unixtimestamp(self, data):
        #time.tzset()
        #1970-01-01T00:00:00Z
        #the_time = time.strptime(data,"%Y-%m-%dT%H:%M:%SZ")
        #time.strftime("%Y-%m-%d %H:%M:%S %Z %z", the_time) 
        #time.mktime(the_time)
        the_time = datetime.datetime.strptime(data, "%Y-%m-%dT%H:%M:%SZ").timestamp()
        self.__timestamp = int(the_time)
        print(str(self.__timestamp))

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
        seconds = int(self.__balance/1000000*60*60)
        # get license out of data
        license = data.get("lic")
        # get stime out of data
        stime = data.get("ts")
        # calculate endtime stime unixtime + seconds
        etime = stime + seconds
        self.__bookings.append({"lic":license,"ts":stime,"te":etime})
        print("New booking:" + str(self.__bookings[-1]))

    def check_booking(self):
        temp1 = self.__bookings
        temp2 = False
        for i in self.__bookings:
            x = int(time.time())
            if i["ts"] < x:
                if i["te"] > x:
                    temp2 = True
                else:
                    temp1.remove(i)
                    print("Time is over, booking deleted!")
        if temp2 == True:
            self.__reserved = True
        else:
            self.__reserved = False
        self.__bookings = temp1
        return self.__reserved

    def print(self):
        print(self.__id)
        print(self.__channelid) 
        print(self.__iotaaddress)





   

    


