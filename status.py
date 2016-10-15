import sys
import RPi.GPIO as GPIO

def main():
	GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

	GPIO.setup(27, GPIO.IN)  # set up pin 17

	state = GPIO.input(27)

	print(state)
	sys.stdout.flush()

	GPIO.cleanup()

main()
