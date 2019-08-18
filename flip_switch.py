import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

switch_1 = 23
switch_2 = 24
switch_3 = 22
switch_4 = 27

GPIO.setup(switch_1, GPIO.IN)
GPIO.setup(switch_2, GPIO.IN)
GPIO.setup(switch_3, GPIO.IN)
GPIO.setup(switch_4, GPIO.IN)

while True:
  if GPIO.input(25):
    GPIO.output(18, False)
  else:
    print "Switch bank: {0}{1}{2}{3}".format(GPIO.input(switch_1), GPIO.input(switch_2), GPIO.input(switch_3), GPIO.input(switch_4))
    GPIO.output(18, True)
  time.sleep(0.5)

