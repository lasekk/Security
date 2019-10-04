'''
Created on 24 Jul 2017

@author: Lasek
'''
import socket

target = input("Enter the IP address to scan: ")
portrange = input("Enter the port range(i.e. 1-100): ")

lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])

print("Scanning host ", target, " from port ", lowport, " to port ",highport, "...")
for port in range(lowport, highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target,port))

    if(status == 0):
        print("*** Port ", port, "- OPEN ***")
    if(status != 0):
        print("*** Port ", port, "- CLOSED***")
    s.close()