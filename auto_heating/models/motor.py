import RPi.GPIO as GPIO
import time


class Servomotor(object):

    def __init__(self):
        self.interval = 0.5
        self.pin = 14
        self.freq = 50

    def move(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.pin, GPIO.OUT)
        servo = GPIO.PWM(self.pin, self.freq)

        # init
        servo.start(0.0)

        servo.ChangeDutyCycle(2.5)
        time.sleep(self.interval)

        servo.ChangeDutyCycle(10.0)
        time.sleep(self.interval)

        GPIO.cleanup()
