
#Tabulatron on PI
# Needs python3

from settings import *
from gpiozero import LED, Button
from time import sleep
from datetime import datetime
#import requests

#Status LED on GPIO 17
status = LED(17)

# Six buttons connected to close GPIOS
b1 = Button(18)
b2 = Button(22)
b3 = Button(24)
b4 = Button(5)
b5 = Button(12)
b6 = Button(19)



#unique light sequence for bootup
def good_status():
	status.on()
	sleep(.5)
	status.off()
	sleep(.5)
	status.on()
	sleep(.5)
	status.off()
	sleep(.5)


#short blinks good
def boot_seq():
	status.on()
	sleep(1)
	status.off()
	sleep(1)
	status.on()
	sleep(1)
	status.off()
	status.on()
	sleep(1)
	status.off()
	sleep(1)
	status.on()
	sleep(1)
	status.off()

#log button presses to make sure they all work
def log(b):
	l = open('button_log.log','a+')
	l.write(str(datetime.now())+" , "+str(b)+"\n")
	l.flush()
	l.close()

#Just let's make sure connectivity is up
def check_connect():
	log("connection_test")
	good_status()


if __name__ == "__main__":
	boot_seq()
	while True:
		if b1.is_pressed:
			print("b1")
			good_status()
			#r = requests.get(BUTTON_1)
			log(BUTTON_1)
		if b2.is_pressed:
			print("b2")
			good_status()
			#r = requests.get(BUTTON_2)
			log(BUTTON_2)
		if b3.is_pressed:
			print("b3")
			good_status()
			#r = requests.get(BUTTON_3)
			log(BUTTON_3)
		if b4.is_pressed and not b6.is_pressed:
			print("b4")
			good_status()
			#r = requests.get(BUTTON_4)
			log(BUTTON_4)
		if b5.is_pressed:
			print("b5")
			good_status()
			#r = requests.get(BUTTON_5)
			log(BUTTON_5)
		if b6.is_pressed and not b4.is_pressed:
			print("b6")
			good_status()
			#r = requests.get(BUTTON_6)
			log(BUTTON_6)
		if b6.is_pressed and b4.is_pressed:
			check_connect()
	sleep(2)