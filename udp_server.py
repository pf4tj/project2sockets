#!/usr/bin/env python3

# The server code that keeps a queue of students waiting,
# and notifies students when they have reached the head of the queue.

# Get command line argument
#
# # Array to keep keep track of queued clients

#

#
# # Setup socket

#
# # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
import socket
from socket import *
import sys
from collections import deque
import queue
import keyboard

port = int(sys.argv[1])
serverName = "127.0.0.1"
BUFFERSIZE = 1024
# clients = []
clients = queue.Queue()
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
HOST = ''
server_address = "localhost"
s.bind((server_address,port)) #initiates connection with port specified.
listen(1)
print ("Server is ready to receive data...")
while True:
        (message, address) = s.recvfrom(BUFFERSIZE)
        # s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        clients.put(message)
        s.send("hello world")
# except:
# conn, addr = s.accept()
# print('Connected by, ', addr)
# except:

      # newConnection, client = s.accept()
#       msg = newConnection.recv(BUFFER_SIZE)
#
#       newConnection.send("hello world")
#       newConnection.close()
s.detach()
s.close()

#s.accept()



# # s.listen(5)
# # s.connect((host,port))
# #
# # # Continuously receive packets
# # server_socket.listen(5) #queue up to 5 connect requests
# while True:
#     s.listen()
#     (message, address) = s.recvfrom(1024) #buffer size
#     Q.put(message)
#     print ("received message : ", message)
    #keep track of first or second message.
    #after servicing the client
    #if key press
#    clients.append(message)
#     s.sendto((message,(address),'80'))

    #

    # Handle the message correctly. Check if this client needs to be added or
    # removed from the queue, and if a new client needs to be notified.
