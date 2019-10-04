'''
Created on 24 Jul 2017

@author: Lasek
'''

'''
Created on 24 Jul 2017

@author: Lasek
'''

import socket

SERVER_ADDRESS = input("Type the server IP address: ")
SERVER_PORT = int(input("Type the server port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_ADDRESS, SERVER_PORT))

print("Connection Established!")

message = input("Message to send: ")

s.sendall(message.encode())
s.close()
