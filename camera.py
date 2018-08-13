from picamera import PiCamera
from time import sleep
import sys


camera = PiCamera()

def main():
    
    camera.start_preview()
    sleep(2)
#camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    camera.stop_preview()
    camera.capture('/home/pi/Desktop/imagecool.jpg')
main()
    
