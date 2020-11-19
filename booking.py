# this module implements functions to check the iota adresses for new bookings
# the function booking() runs a thread in the mainfile

# **********includes*********** #

# include libraries
import json
import time
import iota
import globals
import pprint
import jsonschema 

# include functions

# include classes 
from parkingmeter import ParkingMeter
from wallet import Wallet
from iota import Iota
from iota import Iota, Address
from iota.codecs import TrytesDecodeError
from iota import TryteString
from jsonschema import validate


# ********initialization********* #

# define variables
wallet = Wallet()

# generate a new seed, only for Prototype, there must be a static defined seed in future 
seed = wallet.get_seed()

# set security level
security_level = 2

# set up iota api with node connection
api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)

# json schema that we expect
message = {"uid": "string","lic": "string","ts": "number"}

# **********functions*********** #

# define functions
def newaddress():
    #x = wallet.get_address()
    x = api.get_new_addresses(index=globals.address_index, count=1, security_level = security_level)['addresses'][0]
    globals.address_index += 1
    return x 

# this function validates the json message
def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=message)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# define thread function
def booking():
    while(True):

        # check the balances all 4 seconds is enough
        time.sleep(4)

        # get a list of all license plates in the container
        # elements = globals.container.get_all_elements()
        
        # get a list of the iota adresses of the license plates 
        # list has the same order as license plate index
        addresses = globals.container.get_iota_adress_list()

        #print(addresses[0]) # debug
        #print(addresses[1]) # debug

        # check balance of all addresses in the list
        balances = api.get_balances(addresses, None)

        # set address balance attribute of all license plate elements 
        globals.container.set_balances(balances.get("balances"))

        # init list of addresses that received a transaction
        tx = []
            
        # first, get a list of addresses that received money "output transactions"
        for i in range(len(addresses)):
            if balances.get("balances")[i]>0:
                # get back the transaction object of address i from tangle
                print(addresses[i])
                tx.append(addresses[i]) 

        # second, ask node for transaction objects (list) that we have filtered out
        print(tx) 
        respond = api.find_transaction_objects(tx)
        print(respond)
        print(respond.get("transactions"))


        # third, check all responds for validity and save data
        for i in respond.get("transactions"):
            if i is None:
                print('(Failure: Transaction without booking!)')
            else:
                # print(i) # debug
                for o in i["transactions"]:
                        data = o.signature_message_fragment.decode(errors='ignore')
                        #print(data)
                        if(validateJson(data)):
                            "There is a valid transaction"
                            # convert string to dic
                            data = json.loads(data)
                            uid = data.get("uid")
                            element = globals.container.get_element_by_id(uid)
                            element.set_booking(data)
                        else: 
                            "The transaction is not valid!"
                        print(data)
            













        '''  
        # This is the old version of checking Tangle messages. Problem we make lots of requests to node! 
        # if balance > 0 check then it's an output message for booking
        # we search for output transactions to our iota address
        # output transactions can have a message which is used for
        # sending start time, end time and license number
        for i in range(len(addresses)):
            if balances.get("balances")[i]>0:
                # get back the transaction object of address i from tangle
                addy = addresses[i]
                print(addy)
                transaction = api.find_transaction_objects(addresses=[addy])
                if transaction is None:
                    print('(Failure: Transaction without booking!)')
                else:
                    print("There is a valid transaction!")
                    for tx in transaction["transactions"]:
                        data = tx.signature_message_fragment.decode(errors='ignore')
                        print(data)
                # if there was a value transaction we need a new address
                x = newaddress()
                elements[i].set_iota_address(x)
        '''
