
# This is the Iota Wallet class file

# **********includes*********** #

from iota import Iota
import json
import pathlib


# **********class************** #

class Wallet(object):

    __seed = ""

    __api = Iota('https://nodes.devnet.iota.org:443', __seed, testnet = True)
    
    __security_level = 2

    __counter = 0
    

    def __init__(self):
        # get the current working directory
        path = str(pathlib.Path(__file__).parent)
        # get init file data and build our parkingmeters container #home/ubuntu
        with open(path + "/init.txt") as json_file:
            data = json.load(json_file)
            self.__seed = data["SEED"]

    def get_seed(self):
        return self.__seed
    
    def set_seed(self, seed):
        self.__seed = seed
    
    def get_address(self):
        is_spent = 1
        while is_spent == 1:
            address = self.__api.get_new_addresses(self.__counter, count=1, security_level = self.__security_level)['addresses'][0]
            is_spent = self.__api.were_addresses_spent_from([address])['states'][0]
            self.__counter+1
        return address


