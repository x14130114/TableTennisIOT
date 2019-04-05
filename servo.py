import RPi.GPIO as GPIO
import time

class Servotube:

    def __init__(self):
        pass

    def SetAngle(self, angle):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        # Pin 7 for PWM with 50Hz
        p = GPIO.PWM(11, 50)

        # Start the servo motor at 7.5 angle (center)
        p.start(9.7)
        time.sleep(0.2)
        duty = angle / 18 + 2
        GPIO.output(11, True)
        p.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(11, False)
        p.ChangeDutyCycle(0)
        #print(angle)
        GPIO.cleanup()


    """def cleanup(self):
        p.stop()
        GPIO.cleanup()"""
