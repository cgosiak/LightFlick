import sys
import RPi.GPIO as GPIO

def main():
	GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

	GPIO.setup(17, GPIO.OUT)  # set up pin 17
	GPIO.setup(22, GPIO.OUT)  # set up pin 22

	GPIO.output(17, 0)  # turn off pin 17
	GPIO.output(22, 0)  # turn off pin 17

	print("OFF")

	sys.stdout.flush()
main()
