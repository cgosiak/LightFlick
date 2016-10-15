import sys
import RPi.GPIO as GPIO

def main():
	GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

	GPIO.setup(17, GPIO.OUT)  # set up pin 17

	GPIO.output(17, 1)  # turn on pin 17

	print("Turning Light On!")
	sys.stdout.flush()

main()
