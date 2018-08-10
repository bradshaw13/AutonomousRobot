#Version 0 of Autonomous Go Pi Go
#The following code is for my internship at Jenkinson Enterprises
#The only sensor being used is the ultrasonic sensor the robot can
#autonomously avoid objects and go around them
#I am using a RaspberryPi with a gopigo3 and grovepi stacked on top
# Author: Alexander Bradshaw

import easygopigo3 as easy
import time
import sys
from picamera import PiCamera

camera = PiCamera()

port1 = "AD1"
port2 = "AD2"

gpg = easy.EasyGoPiGo3()

uss = gpg.init_ultrasonic_sensor(port1)
pir = gpg.init_motion_sensor(port2)
servo = gpg.init_servo("SERVO1")
lefts = 0
rights = 0



#when called the robot will stop, then exit the code 
def Exit():
    gpg.stop()
    gpg.reset_encoders(True)
    sys.exit()

#The Around function will turn the robot to avoid the object in front of it    
def Around():
    while True:
        
        servo.rotate_servo(0)
        time.sleep(1)
        rights = uss.read()
        print("right side read ", rights)
        time.sleep(1)
        servo.rotate_servo(180)
        time.sleep(1)
        lefts = uss.read()
        time.sleep(1)
        print("left side read", lefts)
        servo.reset_servo()
        time.sleep(1)
        print("Right side value = ", rights, " Left side value = ", lefts) 
        break
    print("Current read of uss", uss.read())

    
    while uss.read() < 15:
        if lefts < rights and rights > 15:
            gpg.turn_degrees(30)
            #time.sleep(1)
            print("I am turning right 10 degrees")
        elif rights < lefts and lefts > 15:
            gpg.turn_degrees(-30)
            #time.sleep(1)
            print("I am turning left 10 degrees")
        elif rights == lefts and rights > 15:
            gpg.turn_degrees(30)
            #time.sleep(1)
            print("objects equal amount away going right")
        #elif lefts < 15 and rights < 15 and uss.read < 15:
         #   gpg.drive_cm(-15, True)
          #  gpg.turn_degrees(90)
        else:
            gpg.drive_cm(-20, True)
            gpg.turn_degrees(90)
            print("breaking")
            break
        
    return
        

try:
    print("GoPiGo3 Autonomous Robot")
    servo.reset_servo()

    #make sure voltage is high enough if not will exit the code
    if gpg.volt() < 9:
        print("Battery voltage is below 9V; Charge batters")
        Exit()

    #the robot will move forward unless there is an object within 15cm
    #of the robots ultrasonic sensor. If there is then it will take a
    #picture of the object in front of the robot using the picamera then
    #will call the Around function
    while True:
        if uss.read() < 15:
            gpg.stop()
            print("I need to go around the object")
            Around()
            camera.capture('/home/pi/Desktop/intheway.jpg')
                

            #if uss.read() < 100 and pir.motion_detected:
             #   gpg.stop()
                

        else:
            gpg.forward()
    

except IOError as error:
            print('IO error')
    
except KeyboardInterrupt:
    print("\nCtrl+C. Exiting.")
    gpg.stop()
    Exit()
