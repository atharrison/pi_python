import RPi.GPIO as GPIO
import time

led_pin = 4
button_pin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

switch_1 = 23
switch_2 = 13
switch_3 = 6
switch_4 = 5

GPIO.setup(switch_1, GPIO.IN)
GPIO.setup(switch_2, GPIO.IN)
GPIO.setup(switch_3, GPIO.IN)
GPIO.setup(switch_4, GPIO.IN)

while True:
  if GPIO.input(button_pin):
    GPIO.output(led_pin, False)
  else:
    print("Switch bank: {0}{1}{2}{3}".format(GPIO.input(switch_1), GPIO.input(switch_2), GPIO.input(switch_3), GPIO.input(switch_4)))
    GPIO.output(led_pin, True)
  time.sleep(0.5)

