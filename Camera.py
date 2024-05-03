# https://raspberrytips.com/picamera2-raspberry-pi/
import time
from picamera2 import Picamera2, Preview
import libcamera
from datetime import datetime


def takePhoto():
    picam = Picamera2()
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print("Current date & time : ", current_datetime)
    config = picam.create_still_configuration({"size": (1944, 1944)})

    picam.configure(config)
    
    picam.start()
    #time.sleep(0)
    path = "images/" + current_datetime + ".jpeg"
    picam.capture_file(path)

    picam.close()
    
    
takePhoto()
