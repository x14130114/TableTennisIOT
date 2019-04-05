import sys
from self import self
from servo import Servotube
from accel import Accelerometer
from firebase import Firebase
from airshooter import Airshooter
import RPi.GPIO as GPIO
from threading import Thread
import time

# creating objects for other methods in seperate classes
servo = Servotube()
fb = Firebase()
accel = Accelerometer()
airshooter = Airshooter()

# get method
def get():
    oldpos = ""
    while True:
        try:
            print("Starting the loop for checking values on Firebase")
            data = fb.db.get().val()
            # getting sensor values
            servotube = data['sensors']['servotube']['angle']
            servoair = data['sensors']['servoair']['power']
            print(servotube)

            # checking if the servo tube has changed position, move if so
            if servotube == oldpos:
                print ("there was no change to the servo motor")
            elif servotube == "right":
                print ("right turn")
                Servotube.SetAngle(self, 100)
                oldpos = "right"
            elif servotube == "center":
                print ("center position")
                Servotube.SetAngle(self, 120)
                oldpos = "center"
            elif servotube == "left":
                print("left turn")
                Servotube.SetAngle(self, 140)
                oldpos = "left"
            #time.sleep(1)

            # checking if the servo air shooter has changed value, shoot if so
            if servoair == "high":
                print ("HIGH POWER: Shooting Air")
                Airshooter.SetPower(self, 190)
                time.sleep(.2)
                Airshooter.SetPower(self, 120)
                #oldairpos = "high"
                readings = {'sensors/servoair/power': "none"}
                fb.db.update(readings)
            elif servoair == "low":
                print ("LOW POWER: Shooting Air")
                Airshooter.SetPower(self, 140)
                Airshooter.SetPower(self, 120)
                #oldairpos = "low"
                readings = {'sensors/servoair/power': "none"}
                fb.db.update(readings)

        except KeyboardInterrupt:
            #p.stop()
            GPIO.cleanup()
            threadGet.join()
            threadSend.join()
            print ("Interrupted")
            sys.exit(0)

# send method to gather the sensor readings if that status of the sensor is set to 1
# updates firebase with the sensor readings that have a state of 1
def send():
    while True:
        readings = {}
        print ("Sending Accelerometer Values to Firebase...")
        readings['sensors/accelerometer/x-y-z'] = accel.get()
        readings['sensors/accelerometer/speed'] = accel.acceleration()
        #readings['sensors/accelerometer/y'] = accel.get()
        #readings['sensors/accelerometer/z'] = accel.get()
        fb.db.update(readings)
        time.sleep(2)

# running the main
if __name__ == '__main__':
    # setup threads
    threadGet = Thread(target=get)
    threadSend = Thread(target=send)
    # start threads
    threadGet.start()
    threadSend.start()
    # join threads
    threadGet.join()
    threadSend.join()