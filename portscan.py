# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:06:24 2020

@author: Lauren Tooth
"""

import socket
import subprocess
import sys
import time

#function to validate port number input
def inputNumber(message):
    portNumber = input(message)
    if not portNumber.isdigit():
        return inputNumber("Not an integer! Please input a valid port number: ") #message to alert user that an integer value has not been entered
       
    else:
        #check if port entered is in the range of possible port numbers.
        if int(portNumber) > 65535 or int(portNumber) < 1:
            return inputNumber("Out of range. Please input a valid port number: ") #message to alert user the number entered is out of range
        else:        
            return int(portNumber) #return valid value
        

#clear screen
subprocess.call('clear', shell=True)

#ask for input
print ('Welcome to PyNetScan!')
remoteServer = input("Enter host to scan: ")


remoteServerIP = socket.gethostbyname(remoteServer)


#input port numbers
port1 = inputNumber("Please enter the first port number to scan: ")
port2 = inputNumber("Please enter the final port number to scan: ")

#while loop to evaluate if the first port number inputted is smaller than the final port number.
while port1 > port2:
    print ('First port specified must be smaller than the final port specified. Please try again.') #error message
    port1 = inputNumber("Please enter the first port number to scan: ")
    port2 = inputNumber("Please enter the final port number to scan: ")


#print information
print ("-" * 60)
print ("Please wait, scanning host", remoteServerIP)
print ("-" *60)


port3 = port2 + 1

#check current time
t1 = time.time()

try:
    for port in range (port1, port3): #loop to ensure all ports specified are scanned.
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: Open".format(port)) #show port is open
        else:
            print ("Port {}: Closed. ".format(port)) #show port is closed
        sock.close()
except KeyboardInterrupt: #user presses key on keyboard.
    print ("You cancelled the process.")
    sys.exit()

except socket.gaierror: #if there is an error with the hostname.
    print ("Hostname could not be resolved. Exiting...")
    sys.exit()

except socket.error: #if there is no response from host.
    print ("Couldn't connect to server.")
    sys.exit()

#check time again
t2 = time.time()

total = t2 - t1

#output time taken to perform scan
print ("Scan completed in: ", total)