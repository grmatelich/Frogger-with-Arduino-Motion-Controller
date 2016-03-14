#!/usr/bin/env python

PORT = '/dev/cu.usbserial-A40081B5'

import serial
import os
import threading
import sys

def _loop(controller):
	while True:
	    #reading from device	
	    c = controller.device.read(1)
	
	    #if its a new line character, reset the current line, otherwise append the character 'c'
	    if c == '\n':
		try:
		    vals = [int(s) for s in controller.line.split(',')]
		    controller.pitch, controller.roll = int(vals[0]),int(vals[1])
		except:
		    None
	        controller.line = ''
	    else:
	        controller.line += c


class Controller:

    def __init__(self):
	#Sets up connection to arduino
	#from stack overflow exmaple
        """
        def get_serial_port():
            return "/dev/"+os.popen("dmesg | egrep ttyACM | cut -f3 -d: | tail -n1").read().strip()
        """
    	#create a device (arduino connection)
    	self.device = serial.Serial(PORT, baudrate=9600, timeout=3)

	self.line = ''

	self.pitch, self.roll = 0, 0

	self.thread = threading.Thread(target = _loop, args = (self,))
	self.thread.daemon = True
    
    def start(self):
	#Starts the thread running
	self.thread.start()

    def getAction(self):
	#Returns pitch and roll	
	return self.pitch, self.roll

    def close(self):
	#closes the port
	self.device.close()

if __name__ == '__main__':
    controller = Controller()
    controller.start()
    while True:
	print(controller.getAction())
