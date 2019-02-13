#!/usr/bin/env python3

import socket
import random
import string
import time
# creates socket object
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
host = socket.gethostname() #localhost or ''
port = 21212

s.connect((host, port))
while True:     
    message = s.recv(1024) # msg can only be 1024 bytes long
    if not message:
            print('there is no data')
            break
    message = message.decode()
    start = message.find('PASSWORD=')
    if (start != -1):
        message = message[start + 9:]
        end  = message.find('.')
        print('Password is :', message[:end])
        break

s.close()
# print("the time we got from the server is %s" % message.decode('ascii'))