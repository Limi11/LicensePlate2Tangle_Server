# here we define global variables and objects  

from container import Container
from threading import Event


def container_init():
    global container 
    container = Container()

def event_init():
    global receive_data
    receive_data = Event()