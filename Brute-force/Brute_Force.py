'''
Created on 31 Jul 2017

@author: Lasek

To be completed...

'''

import http.client


SERVER_ADDRESS = input("Type the server IP address: ")
SERVER_PORT = input("Type the server port: ")
URL = input("Type the URL: ")
if(SERVER_PORT == ""):
    SERVER_PORT = 80
        
print("Connection Established!")

try: 
    connection = http.client.HTTPConnection(SERVER_ADDRESS, SERVER_PORT)
    connection.request('GET', URL)
    response = connection.getresponse()
    print("\nServer response: ", response.status)
    connection.close()
except ConnectionRefusedError:
    print("\nConnection Failed...")