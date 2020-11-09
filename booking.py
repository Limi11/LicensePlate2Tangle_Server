
# tnis function is checking if there are new bookings on the python addresses

# includes 
from iota import Iota
from wallet import Wallet

# define variables
wallet = Wallet()

# define functions
def newaddress():
    x = wallet.get_address()
    return x 

# define thread function
def booking():
    seed = wallet.get_seed()
    adresses = ["DE9DVSOWIIIKEBAAHCKBWNXGXTOKVLZPLRAGKZG9GXKFRFWERKBFYMPRLAGVZTRVYPEPHBMUPDMRQ9DPZ","DE9DVSOWIIIKEBAAHCKBWNXGXTOKVLZPLRAGKZG9GXKFRFWERKBFYMPRLAGVZTRVYPEPHBMUPDMRQ9DPZ"]
    api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)
    balances = api.get_balances(adresses, None)
    address = newaddress()
    print(balances)
    print("new address:", address)