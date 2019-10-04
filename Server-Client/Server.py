'''
Created on 24 Jul 2017

@author: Lasek
'''

import socket

SERVER_ADDRESS = input("Type the server IP address: ")
SERVER_PORT = int(input("Type the server port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER_ADDRESS, SERVER_PORT))
s.listen(1)

print("Server started! Waiting for connections...")
connection, address = s.accept()

print("Client connected with address: ", address)

while 1:
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b'-- Message Received --\n')
    print(data.decode('utf-8'))
connection.close()