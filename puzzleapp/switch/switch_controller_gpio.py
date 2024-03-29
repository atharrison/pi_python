import random
try:
    import RPi.GPIO as GPIO
except ImportError:
    pass
import time

led_pin = 4
button_pin = 17

# Map the GPIO inputs to the switches
switch_bank_bcm = [12,16,20,21,23,13,6,5]

class SwitchControllerGPIO():

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(led_pin, GPIO.OUT)
        GPIO.setup(button_pin, GPIO.IN)

        for i in range (0, len(switch_bank_bcm)):
            GPIO.setup(switch_bank_bcm[i], GPIO.IN)

        self.switches = [0, 0, 0, 0, 0, 0, 0, 0]

    def switch_data(self):
        # Read switch values into self.switches
        for i in range(0, len(switch_bank_bcm)):
            # Note: Physically, switches are placed backwards.
            # So report opposite.
            self.switches[i] = int(not GPIO.input(switch_bank_bcm[i]))

        return self.switches

    def is_button_pushed(self):
        if GPIO.input(button_pin):
            GPIO.output(led_pin, False)
            return False
        else:
            GPIO.output(led_pin, True)
            return True

    def blink_button_fast(self):
        blink_rate = 0.1
        for i in range(0,5):
            GPIO.output(led_pin, True)
            time.sleep(blink_rate)
            GPIO.output(led_pin, False)
            time.sleep(blink_rate)

    def input_as_string(self):
        return "".join(map(str, self.switch_data()))

    def input_as_array(self):
        return self.switch_data()

    def simulate_button_push(self):
        # Do nothing.
        # Only here to conform
        # in case I leave in the task that auto-pushes the button
        pass
