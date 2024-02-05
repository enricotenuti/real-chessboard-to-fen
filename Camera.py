# https://raspberrytips.com/picamera2-raspberry-pi/
import time
from picamera2 import Picamera2, Preview
import libcamera


def takePhoto():
    picam = Picamera2()

    config = picam.create_still_configuration({"size": (1944, 1944)})

    picam.configure(config)

    picam.start()
    #time.sleep(0)
    picam.capture_file("images/current_board.jpeg")

    picam.close()
