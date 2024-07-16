'''
This file is written by SEGP Group 7b
This file is to set up IP camera for live capturing
'''

import cv2
import numpy as np
import time
import os
        
#Function to take an image of current camera frame    
def takeImage(filename):
    #Start up camera module
    try:
        
        cap = cv2.VideoCapture(0)
        
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)
        
        ret, frame = cap.read()
        
        #Set folder path to save image captured in
        path = '/home/pi/Desktop/PI_SEGP/resources/temp/current_input'
        cv2.imwrite(os.path.join(path, filename),frame)
        
        ori = '/home/pi/Desktop/PI_SEGP/original'
        cv2.imwrite(os.path.join(ori, filename), frame)
        
        #Turn off camera module
        cap.release()
    except:
        #Error message if camera is not working
        messagebox.showerror("Error", "Camera not found")