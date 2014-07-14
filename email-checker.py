import sys
import serial
import gmaillib
import time

def readSerial():
	# Wait for Arduino to report it is ready before starting as windows will reset the arduino
	line = ""
	while True:
	    for c in com.read():
	        line += c
	        if c == '\n':
	            return

def setLEDOn(state):
	if state:
		com.write("on;")
	else:
		com.write("off;")

# Open serial coms
com = serial.Serial(2, 9600)
# Wait for arduino to be ready
readSerial()

gmail = gmaillib.account("andycampbell92", "S1E$#YvNTI2z")
while True:
	unread = gmail.unread()
	if len(unread) > 0:
		setLEDOn(True)
		print "unread"
	else:
		print "read"
		setLEDOn(False)
	time.sleep(5)