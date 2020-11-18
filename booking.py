# this module implements functions to check the iota adresses for new bookings
# the function booking() runs a thread in the mainfile

# **********includes*********** #

# include libraries
import json
import time
import iota
import globals

# include functions

# include classes 
from parkingmeter import ParkingMeter
from wallet import Wallet
from iota import Iota

# ********initialization********* #

# define variables
wallet = Wallet()

# generate a new seed, only for Prototype, there must be a static defined seed in future 
seed = wallet.get_seed()

# set security level
security_level = 2

# set up iota api with node connection
api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)


# **********functions*********** #

# define functions
def newaddress():
    #x = wallet.get_address()
    x = api.get_new_addresses(index=globals.address_index, count=1, security_level = security_level)['addresses'][0]
    globals.address_index += 1
    return x 

# define thread function
def booking():
    while(True):

        # check the balances all 4 seconds is enough
        time.sleep(4)

        # get a list of all license plates in the container
        elements = globals.container.get_all_elements()
        
        # get a list of the iota adresses of the license plates
        addresses = globals.container.get_iota_adress_list()

        print(addresses[0])
        print(addresses[1])

        # check balance of all addresses in the list
        balances = api.get_balances(addresses, None)
            
        # if balance > 0 check then it's an output message for booking
        # we search for output transactions to our iota address
        # output transactions can have a message which is used for
        # sending start time, end time and license number
        for i in range(len(addresses)):
            if balances.get("balances")[i]>0:
                # get back the transaction object of address i from tangle
                message = api.find_transaction_objects(addresses[i])
                if message is None:
                    print('(Failure: Transaction without booking!)')
                else:
                    print(message.decode())
                # if there was a value transaction we need a new address
                x = newaddress()
                elements[i].set_iota_address(x)
        



#adresses = ["DE9DVSOWIIIKEBAAHCKBWNXGXTOKVLZPLRAGKZG9GXKFRFWERKBFYMPRLAGVZTRVYPEPHBMUPDMRQ9DPZ","DE9DVSOWIIIKEBAAHCKBWNXGXTOKVLZPLRAGKZG9GXKFRFWERKBFYMPRLAGVZTRVYPEPHBMUPDMRQ9DPZ"]
#print(balances)
#print("new address:", address)
