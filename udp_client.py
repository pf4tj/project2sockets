#!/usr/bin/env python3
from socket import *
import socket
import sys
import msvcrt as m
def wait():
    m.getch()

# The client code that requests a spot in the queue, a
# nd notifies the server when the student is finished getting help during office hours.

# Get command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
name = sys.argv[3]

# The client, when run, must notify the server that a new student wants to join the office hours queue.
# The client must then wait for the server to notify it that it is now at the head of the queue.
# The client then must notify the server when the student is finished by waiting for any input on stdin and then
# sending a packet to the server. At that point the client can safely exit.


# Create a socket and notify the server we want to be added to the office
# hour queue.

servername = 'localhost'
BUFFERSIZE = 1024

s = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM)

#s.connect((servername,port))
#s.bind((host, port))
sendMessage = name
closeFlag = False
firstInstance = True
# do while loop maybe so it executes at least once
while True:

    print("Client sending", sendMessage)
    s.sendto(sendMessage.encode(), (host,port))

    print("Waiting on server response")
    recvMessage = s.recv(BUFFERSIZE)
    recvMessage = message.decode()

    if (recvMessage == name):
        x = input("At head of queue, press Enter to indicate you are finished getting help.")

        if(x == ""):
            sendMessage="XXXXXX"
            print("Sending remove response to server")
    elif(recvMessage == "XXXXXX"):
        break
    else:
        x = input("Not at head of queue, press enter to try again")

        if(x == ""):
            continue

s.close()



# # s.sendto(message, host,port)


# # (host, port)

# # print(host)

# # Wait for head of queue message from the server.



# # Wait for user to signal that we are done (via stdin) and notify the server.
