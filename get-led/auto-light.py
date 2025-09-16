import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
fototr = 6
GPIO.setup(fototr, GPIO.IN)

while True:
    if GPIO.input(fototr) == 0:
        GPIO.output(led, 1)
        time.sleep(1)
    else:
        GPIO.output(led, 0)
        time.sleep(1)