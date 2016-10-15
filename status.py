import sys
import RPi.GPIO as GPIO

def main():
	GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

	GPIO.setup(17, GPIO.IN)  # set up pin 17

	state = GPIO.input(17)

	print(state)
	sys.stdout.flush()

main()
