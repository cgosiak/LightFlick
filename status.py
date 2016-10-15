import sys
import RPi.GPIO as GPIO

def main():
	GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

	GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # set up pin 17
	# GPIO.setup(22, GPIO.OUT)  # set up pin 17

	# GPIO.output(22, 0)


	status = GPIO.input(27)  # turn off pin 17
	print(status)

	sys.stdout.flush()


main()
