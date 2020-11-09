
# this function is listening for sensor data 
# socket communication see https://realpython.com/python-sockets/

# **********includes*********** #

# include libraries
import json
import socket
import selectors
import types

# define variables
HOST = "127.0.0.1" # localhost ip address for testing 
port = 65432       # port to listen on should be >1024

# the defaultselctor is used to run an event driven multi-connection server
sel = selectors.DefaultSelector()

# inti of TCP server
# AF_INET == IPv4, SOCK_STREAM == TCP
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST,port))
lsock.listen()
print("listening on", (HOST,port))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

# start TCP server for communication with parking meters
def sensordata():
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key,mask)



# internal functions for TCP communication 

def accept_wrapper(sock):
    conn, addr = sock.accept()
    print("accept connection from", addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb += recv_data
        else:
            print("closing connection to", data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print("echoing", repr(data.outb), "to", data.addr)
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]
   


