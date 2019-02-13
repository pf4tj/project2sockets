#!/usr/bin/env python3
import random
import socket
import string
import time
print ('Starting program ...')
while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('', 21212)
        sock.bind(server_address)
        sock.listen(1)
    except: 
        print('failed to create socket ...')
        sock.close()
        break
    print('the server is ready to receive ')
    connection, addr =  sock.accept()
    print('connected by : ', addr)
    while True: 
        message = connection.recv(1024)
        if not message:
            print('there is no data')
            break
        message = message.decode()
        start = message.find('PASSWORD=')
        if (start != -1):
            message = message[start + 9:]
            end  = message.find('.')
            print(message[:end])
            break
    print('Socket closing ... ')
    sock.close()



                    # connection.sendall(data)
            # password = 'Sup3rSecre$'
            # r1 = ''.join(random.choices(string.printable, k=30))
            # r2 = ''.join(random.choices(string.printable, k=20))
            # message = '{}PASSWORD={}.{}'.format(r1, password, r2)
            # print ('encrypted message is : ', message)
            # print('Encrypted message is : ',message, '\n')