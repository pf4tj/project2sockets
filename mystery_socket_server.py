# #!/usr/bin/env python3

# import random
# import socket
# import string
# import time

# print('Run `nc -l 21212` to listen for the output of this example.')

# # Need to keep looping in case nothing is listening for us.
# while True:
#     try:
#         # Create a socket object to emulate the mystery socket.
#         mystery = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#         # Try to connect to the machine to create a socket and send the
#         # mystery data.
#         mystery.connect(('', 21212))

#         mystery.listen(1)

#         while True:
#             # If the connection succeeds then we can send mystery data. This may
#             # not be exactly how the mystery socket works, but it is similar at
#             # least....
#             clientSocket, addr = mystery.accept()
#             print("got a connection from %s" % str(addr))
#             password = 'Sup3rSecre$'
#             r1 = ''.join(random.choices(string.printable, k=30))
#             r2 = ''.join(random.choices(string.printable, k=20))
#             message = '{}PASSWORD={}.{}'.format(r1, password, r2)
#             mystery.send(message.encode('ascii'))

#             # Wait one second before sending more data. This kind of seems like
#             # how the mystery socket works.
#             time.sleep(1)

#     except:
#         # Wait a couple seconds before retrying.
#         time.sleep(2)

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
