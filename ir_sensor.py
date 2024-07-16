'''
This file is written by SEGP Group 7b
This file is to receive the GPIO input and output of Infrared sensor to trigger image capturing
'''

import odroid_wiringpi as wp
import time

# Initialize variable for the output of sensor to 0
# 0 = No object detected
# 1 = Object detected
sensor = 0

# Function to read the signal of IR sensor
def Sensor():
    wp.wiringPiSetup()
    
    # Setup GPIO to read pin 3 (input) and 5 (output)
    wp.pinMode(3, wp.INPUT)
    wp.pinMode(5, wp.OUTPUT)
    
    # Read output of IR sensor at PIN(3)
    val = wp.digitalRead(3)

    # No object detected
    if val == 1:
        wp.digitalWrite(5, wp.LOW)
        sensor = False

    # Object detected
    else:
        wp.digitalWrite(5, wp.HIGH)
        sensor = True

    return sensor
