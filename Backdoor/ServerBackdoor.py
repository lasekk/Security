'''
Created on 31 Jul 2017

@author: Lasek
'''


import socket
import platform
import os

SERVER_ADDRESS = ""
SERVER_PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_ADDRESS, SERVER_PORT))
s.listen(1)

print("Server started! Waiting for connections...")
connection, address = s.accept()

print("Client connected with address: ", address)

while 1:
    try:
        data = connection.recv(1024)
    except:continue
    
    if (data.decode('utf-8') == '1'):
        toSend = "\nSystem: " + platform.platform() + " " + platform.machine()    
        connection.sendall(toSend.encode())       
    elif(data.decode('utf-8') == '2'):
        toSend = "\nPC's network name: " + platform.node()
        connection.sendall(toSend.encode())
    elif(data.decode('utf-8') == '3'):
        data = connection.recv(1024)
        try:
            filelist = os.listdir(data.decode('utf-8'))
            toSend = ""
            for x in filelist:
                toSend += "," + x
        except:
            toSend = "Wrong Path"       
        connection.sendall(toSend.encode())
    elif(data.decode('utf-8') == '4'):
        print("Client disconnected")
        connection.close()
    else:
        toSend = "\nInvalid Option"
        
