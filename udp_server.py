#!/usr/bin/env python3

# The server code that keeps a queue of students waiting,
# and notifies students when they have reached the head of the queue.
cket

#
# # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
import socket
import sys
from collections import deque
import queue
import keyboard

PORT = int(sys.argv[1])
SERVERADDRESS = "localhost"
SERVERPORT = 12000
BUFFERSIZE = 1024

clients = []
serverSocker = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM)
# HOST = ''
serverSocket.bind((SERVERADDRESS,PORT)) #initiates connection with port specified.
serverSocket.listen(5)
print ("Server is ready to receive data...")
#
while True:
        try:
            (message, address) = serverSocket.recvfrom(BUFFERSIZE)
            if not clients:
                print("Queue is empty...")
                clients.append("Hello World")
                break;
            elif clients[0] is str(message):
                serverSocket.sendto(,address)
            else:

                #
            # s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            # if not clients:
            #     clients.append(message)
            # s.send("hello world")
        except:
            s.detach()
            s.close()
for x in clients:
    print (x)
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
