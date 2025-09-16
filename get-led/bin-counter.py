import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
num = 0
sleep_time = 0.2
up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

while True:
    if 0 > num > 2**8:
        break
    if GPIO.input(up):
        num += 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(down):
        num -= 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    GPIO.output(leds, dec2bin(num))