'''
Created on 26 Jul 2017

@author: Lasek
'''
import http.client


print("*** Program displays allowed HTTP methods ***")

ans=True
while ans:
    host = input("Enter IP: ")
    port = input("Enter port (default:80): ")

    if(port == ""):
        port = 80

    try: 
        connection = http.client.HTTPConnection(host, port)
        connection.request('OPTIONS', '/')
        response = connection.getresponse()
        print("\nAllowed methods: ", response.getheader('allow'))
        connection.close()
    except ConnectionRefusedError:
         print("\nConnection Failed...")
         
    ans = input("\nContinue? (y/n): ")
    if ans == "n":
        ans = False