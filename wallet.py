
# includes 
from iota import Iota



class Wallet(object):

    __seed = "JBN9ZRCOH9YRUGSWIQNZWAIFEZUBDUGTFPVRKXWPAUCEQQFS9NHPQLXCKZKRHVCCUZNF9CZZWKXRZVCWQ"

    __api = Iota('https://nodes.devnet.iota.org:443', __seed, testnet = True)
    
    __security_level = 2

    __counter = 0
    
    def get_seed(self):
        return self.__seed
    
    def get_address(self):
        is_spent = 1
        while is_spent == 1:
            address = self.__api.get_new_addresses(self.__counter, count=1, security_level = self.__security_level)['addresses'][0]
            is_spent = self.__api.were_addresses_spent_from([address])['states'][0]
            self.__counter+1
        return address


