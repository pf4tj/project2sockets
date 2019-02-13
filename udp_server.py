#!/usr/bin/env python3

# The server code that keeps a queue of students waiting,
# and notifies students when they have reached the head of the queue.


#
# # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
from socket import *
import socket
import sys
from collections import deque
import queue
# import keyboard

PORT = int(sys.argv[1])
SERVERADDRESS = "127.0.0.1"
BUFFERSIZE = 1024

clients = deque([])
serverSocket = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM)
# HOST = ''
serverSocket.bind((SERVERADDRESS,PORT)) #initiates connection with port specified.
#serverSocket.listen(5)


while True:
        print ("Server is ready to receive data...")
        (message, address) = serverSocket.recvfrom(BUFFERSIZE)
        message = message.decode('UTF-8')
        print("Server recieved", message)

        if(message == "XXXXXX"):
            #serverSocket.sendto(clients[0].encode(),address)
            print(clients[0], "deleted from queue")
            clients.popleft()
        else:
            try:
                clients.index(message)
            except ValueError:
                clients.append(message)
                print(message, "added to queue")
        if(len(clients) > 0):
            serverSocket.sendto(clients[0].encode(), address)
                #
            # s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            # if not clients:
            #     clients.append(message)
            # s.send("hello world")


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
