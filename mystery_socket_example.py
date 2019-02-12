#!/usr/bin/env python3

import random
import socket
import string
import time

print('Run `nc -l 21212` to listen for the output of this example.')

# Need to keep looping in case nothing is listening for us.
while True:
    try:
        # Create a socket object to emulate the mystery socket.
        mystery = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Try to connect to the machine to create a socket and send the
        # mystery data.
        mystery.connect(('', 21212))

        while True:
            # If the connection succeeds then we can send mystery data. This may
            # not be exactly how the mystery socket works, but it is similar at
            # least....
            password = 'Sup3rSecre$'
            r1 = ''.join(random.choices(string.printable, k=30))
            r2 = ''.join(random.choices(string.printable, k=20))
            message = '{}PASSWORD={}.{}'.format(r1, password, r2)
            mystery.send(message.encode())
            start = message.find('PASSWORD=')
            if (start != -1):
                message = message[start + 9:]
                end  = message.find('.')
                print(message[:end])
            # Wait one second before sending more data. This kind of seems like
            # how the mystery socket works.
            time.sleep(1)

            exit(0)

    except:
        # Wait a couple seconds before retrying.
        time.sleep(2)
