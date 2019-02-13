#!/usr/bin/env python3

import random
import socket
import string
import time

# creating a socket object
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

# get local Host machine name
host = socket.gethostname() # or just use (host == '')
port = 21212

# bind to pot
s.bind((host, port))

# Que up to 5 requests
s.listen(1)

while True:
    # establish connection
    clientSocket, addr = s.accept()
    password = 'Sup3rSecre$'
    r1 = ''.join(random.choices(string.printable, k=30))
    r2 = ''.join(random.choices(string.printable, k=20))
    message = '{}PASSWORD={}.{}'.format(r1, password, r2)
    print (message)
    # mystery.send(message.encode('ascii'))
    print("got a connection from %s" % str(addr))
    # currentTime = time.ctime(time.time()) + "\r\n"
    clientSocket.send(message.encode('ascii'))
    clientSocket.close()