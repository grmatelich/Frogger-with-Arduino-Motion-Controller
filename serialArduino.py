#!/usr/bin/env python

import serial 
import sys
import os

#from stack overflow exmaple 
def get_serial_port():
    return "/dev/"+os.popen("dmesg | egrep ttyACM | cut -f3 -d: | tail -n1").read().strip()

"""/dev/tty.usbmodem1411"""
print(get_serial_port())

device = serial.Serial(get_serial_port(), baudrate=9600, timeout=3)

while True:

    line = device.readline()

    if "P" in line:
        index = line.index("P")
        print(line[1: index-1])
        print(line[index+1: ])
        roll = float(line[1: index-1])
        pitch = float(line[index+1: ])

        #sys.stdout.write(roll)
        #sys.stdout.write(" ")
        #sys.stdout.write(pitch)
    result = "%d %d", roll, pitch
    print(result)

s.close()
