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

# include classes 
from parkingmeter import ParkingMeter
from iota import Iota
from iota import Iota, Address
from iota.codecs import TrytesDecodeError
from iota import TryteString
from jsonschema import validate
from threading import Thread, Lock, Event
from wallet import Wallet

# ********initialization********* #

wallet = Wallet()

# get seed for further operations
seed = wallet.get_seed()
#print(seed)

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
        a_json = json.loads(jsonData)
        try: 
            validate(instance=a_json, schema=message)
            return True
        except:
            print("Json message does not fit with requirements!")
    except:
	    print("String could not be converted to JSON")
    return False

# define thread function
def booking():
    while(True):

        # check the balances all 4 seconds is enough
        time.sleep(5)

        # lock thread during access of global container
        globals.mutex.acquire()

        # get a list of all license plates in the container
        elements = globals.container.get_all_elements()
        
        # get a list of the iota adresses of the license plates 
        # list has the same order as license plate index
        addresses = globals.container.get_iota_adress_list()

        # release thread after access of global container
        globals.mutex.release()

        #print(addresses[0]) # debug
        #print(addresses[1]) # debug

        # check balance of all addresses in the list
        balances = api.get_balances(addresses, None)

        # lock thread during access of global container
        globals.mutex.acquire()
        
        # set address balance attribute of all license plate elements 
        globals.container.set_balances(balances.get("balances"))

        # release thread after access of global container
        globals.mutex.release()

        # init list of addresses that received a transaction
        tx = []

        # variable to remember index of elements that received a transaction
        re = []
            
        # first, get a list of addresses that received money "output transactions"
        for i in range(len(addresses)):
           # print(addresses[i])
            if balances.get("balances")[i]>0:
                # get back the transaction object of address i from tangle
                tx.append(addresses[i]) 
                re.append(i)
              

        # second, ask node for transaction objects (list) that we have filtered out
        respond = api.find_transaction_objects(addresses = tx)
        #print(respond)

        # variable to check itteration of following for loop
        iteration = 0

        # lock thread during access of global container
        globals.mutex.acquire()

        # third, check all responds for validity and save data
        for i in respond.get("transactions"):
            if i is None:
                print('(Failure: Transaction without booking!)')
            else:
                data = i.signature_message_fragment.decode(errors='ignore')
                if(validateJson(data)):
                        data = json.loads(data)
                        print("There is a valid transaction")
                        print(data)
                        uid = data.get("uid")
                        element = globals.container.get_element_by_id(uid)
                        if(element == None):
                            print("ID is not registered!")

                        else:
                            element.set_booking(data)
                            element.set_next_booking_start()
                            element.set_next_booking_end()
                       
                else: 
                    print("The transaction is not valid!")
            
            # if there was a value transaction we need a new address
            x = newaddress()
            print("New address: " + x)
            # iteration does not know which elements got a transaction
            # we have saved the index of elements that received a payment 
            # in re[]
            y = re[iteration]
            elements[y].set_iota_address(x)
            iteration =+ 1
          
        # release thread after access of global container
        globals.mutex.release()










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
