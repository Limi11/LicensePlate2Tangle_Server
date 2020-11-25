# here we define global variables and objects  

from container import Container
from threading import Event
from threading import Thread, Lock, Event


def container_init():
    global container 
    container = Container()

def event_init():
    global receive_data
    receive_data = Event()

def addrees_index_init():
    global address_index
    address_index = 0

def mutex():
    global mutex
    # create mutex to be threadsafe
    mutex = Lock()

def hostip():
    global hostip
    # create local host variable
    hostip = "127.0.0.1"

def port():
    global port
    # create global port variable
    port = 65432
