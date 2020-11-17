# this module implements functions to check the iota adresses for new bookings
# the function booking() runs a thread in the mainfile

# **********includes*********** #

# include libraries
import json
import time
import iota

# include functions

# include classes 
from parkingmeter import ParkingMeter
from wallet import Wallet
from iota import Iota
from globals import container


# define variables
wallet = Wallet()

# generate a new seed, only for Prototype, there must be a static defined seed in future 
seed = wallet.get_seed()

api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)

# define functions
def newaddress():
    x = wallet.get_address()
    return x 

# define thread function
def booking():
    while(True):

        # check the balances all 4 seconds is enough
        time.sleep(4)

        # get a list of all license plates in the container
        elements = container.get_all_elements()

        # get size of list
        size = container.get_container_size()
        
        # get a list of the iota adresses of the license plates
        addresses = get_iota_adress_list(size)

        # check balance of all addresses in the list
        balances = api.get_balances(addresses, None)

            
        # if balance > 0 check then it's an output message for booking
        # we search for output transactions to our iota address
        # output transactions can have a message which is used for
        # sending start time, end time and license number
        for i in range(len(balances)):
            if balances > 0:
                message = find_transaction_objects(addresses[i])
                if message is None:
                    print('(None)')
                else:
                    print(message.decode())




# this function gives a list of all used iota adresses back
def get_iota_adress_list(elements):
    addresses = [] 
    for i in range(elements):
            # get parkingmeter object
            licenseplate = container.get_element_by_index(i)
            # get iota address of parkingmeter
            addresses[i] = licenseplate.get_address()
    return addresses




#adresses = ["DE9DVSOWIIIKEBAAHCKBWNXGXTOKVLZPLRAGKZG9GXKFRFWERKBFYMPRLAGVZTRVYPEPHBMUPDMRQ9DPZ","DE9DVSOWIIIKEBAAHCKBWNXGXTOKVLZPLRAGKZG9GXKFRFWERKBFYMPRLAGVZTRVYPEPHBMUPDMRQ9DPZ"]
#
#balances = api.get_balances(adresses, None)
#address = newaddress()
#print(balances)
#print("new address:", address)
