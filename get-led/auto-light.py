import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
fototr = 6
GPIO.setup(fototr, GPIO.IN)
state = 0

while True:
    if GPIO.input(fototr) == 0:
        state = not state
        GPIO.output(led, state)
        time.sleep(1)