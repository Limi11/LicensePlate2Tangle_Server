# This is a testscript for simulation of the smartphone app iota transaction process

# include libraries
import json

# include classes
from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import TryteString

# test data in correct format
testdata = "{\"uid\":\"E24F43FFFE44C3FC\",\"lic\": \"LB-AB-1234\",\"ts\": 1235489}"
#testdata = json.loads(testdata)

# testseed
seed = 'CVBCQHX9MUZZBEAZGOO9GYHWYBEZRMTWNXKBQHNSFETKUPHKHRGUYWLTSGXYAQEVLNI9XTQPTZAGOIUZH'

# devine that we use the devnet
api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)

# check balance of account
balance = api.get_account_data()
print(balance)
#addresses = []
#addresses.append('SVCSKJPIIAOOSAAYMS9HKQVSIRVCKGOFNVQRTEXJNBFMCYFDIEWWYXBWZQDSKNJCVXCQGS9GUJLBHEAVBNS9UNPGFB')
#balances = api.get_balances(addresses, None)
#print(balances)

# address for output transaction
address = 'BMAMHVEKDSOUM9OAFQEKNAMCXOZIH9BNVAKFQYXWNULKMPWRB9GOM9QCHLTR9SZZYCFRPKCCLDYSFDZ9W'

tx = ProposedTransaction(address=Address(address),value = 1, message=TryteString.from_unicode(testdata))


result = api.send_transfer(transfers=[tx])
print('Bundle: ')
print(result['bundle'])




'''
#////////////////////////////////////////////////
#// Generate an unspent address
#////////////////////////////////////////////////

from iota import Iota

# The seed that will be used to generate an address
seed = 'CVBCQHX9MUZZBZAZGOO9GYHWYBEZRMTWNXKBQHNSFETKUPHKHRGUYWLTSGXYAQEVLNI9XTQPTZAGOIUZH'

# Connect to a node
api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)

# Define the security level of the address
security_level = 2

# Generate an unspent address with security level 2
address = api.get_new_addresses(index=0, count=1, security_level = security_level)['addresses'][0]

is_spent = api.were_addresses_spent_from([address])['states'][0]

if is_spent:
    print('Address %s is spent!' % address )
else:
    print('Your address is: %s' % address )
'''