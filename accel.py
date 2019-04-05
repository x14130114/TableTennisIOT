import Adafruit_ADXL345
import time
import math

from self import self


class Accelerometer:
    accel = Adafruit_ADXL345.ADXL345()

    def get(self):
        while True:
            x, y, z = Accelerometer.accel.read()

            f = Accelerometer.e
            try:
                print ('X={0}, Y={1}, Z={2}'.format(x, y, z))
                return 'X={0}, Y={1}, Z={2}'.format(x, y, z)
            except IOError as e:
                print ("Error: Accelerometer: %s." % (e.message,))

    def acceleration(self):
        while True:
            x, y, z = Accelerometer.accel.read()
            try:
                acceleration = math.sqrt(x ** 2 + y ** 2 + z ** 2)
                print(acceleration)
                return acceleration
            except IOError as e:
                print ("Error with calculating Magnitude of Acceleration: %s." % (e.message,))

#while True:
#    try:
#        Accelerometer.get(self)
#        time.sleep(2)
#    except IOError as e:
#        print (e.message)

