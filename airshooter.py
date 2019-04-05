import RPi.GPIO as GPIO
import time

class Airshooter:

    def __init__(self):
        pass

    def SetPower(self, angle):
        # Setting up Servo motor to GPIO pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)

        p = GPIO.PWM(7, 50)

        p.start(7.5)
        print ("Air Shooter")
        duty = angle / 18 + 2
        GPIO.output(7, True)
        p.ChangeDutyCycle(duty)
        time.sleep(0.2)
        GPIO.output(7, False)
        p.ChangeDutyCycle(0)
        GPIO.cleanup()
