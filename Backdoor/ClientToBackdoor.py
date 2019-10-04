'''
Created on 31 Jul 2017

@author: Lasek
'''

import socket

SERVER_ADDRESS = input("Type the server IP address: ")
SERVER_PORT = int(input("Type the server port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_ADDRESS, SERVER_PORT))


print("Connection Established!\n")
def printMenu():
    print("""
    1) Display system
    2) Display PC's Network Name
    3) Insert the path
    4) Quit
    """)

printMenu() 
ans=True
while 1:
    message = input("\n-Select an option: ")

    if(message == '1'):
        s.sendall(message.encode())
        data = s.recv(1024)
        if not data: break
        print(data.decode('utf-8'))
        
    elif(message == '2'):
        s.sendall(message.encode())
        data = s.recv(1024)
        if not data: break
        print(data.decode('utf-8'))   
    elif(message == '3'):
        path = input("Path: ")
        s.sendall(message.encode())
        s.sendall(path.encode())
        data = s.recv(1024)
        data = data.decode('utf-8').split(",")
        print("*" * 40)
        for x in data:
            print(x)
        print("*" * 40)   
    elif(message == '4'):
        s.sendall(message.encode())
        s.close
        break
    printMenu()     