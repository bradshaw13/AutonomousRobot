#Version 2 of Autonomous Robot
#The following code is for my internship at Jenkinson Enterprises
#I am using a RaspberryPi with a GoPiGo3 and GrovePi stacked on top
#Sensors:
#   Ultrasonic Sensor
#   PIR Motion Sensor
#   Both plugged in to GoPiGo3
#Sensors are mounted on a servo panel
#
#PiCamera:
#   The PiCamera will take a picture when there is an object closer than 15cm
#   in front of the robot
#
#Led Lights:
#   When the robot is going forward both lights will be on and
#   when turning the corresponding blinker will turn and the other will
#   be off and when going backwards both lights will be off
#   (Plugged into GrovePi)
#Buzzer:
#   The buzzer will go off when the robot has been boxed in and has to go
#   backwards and when there is motion detected as it is driving forward
#   (Plugged into GrovePi)
#
#Author: Alexander Bradshaw


import easygopigo3 as easy
import time
import sys
from picamera import PiCamera
from grovepi import*

camera = PiCamera()

port1 = "AD1"
port2 = "AD2"

gpg = easy.EasyGoPiGo3()

uss = gpg.init_ultrasonic_sensor(port1)
pir = gpg.init_motion_sensor(port2)
servo = gpg.init_servo("SERVO1")
lefts = 0
rights = 0

#Initializes ports and pinmode for buzzer at Digital Port 3
buz = 8

pinMode(buz, "OUTPUT")

#Initializes ports and pinMode for each of the led lights
#Right blinker is blue(Digital Port 3) and Left blinker is red(Digital Port 2)
led1 = 3
pinMode(led1, "OUTPUT")


led2 = 2
pinMode(led2, "OUTPUT")



#when called the robot will stop, then exit the code 
def Exit():
    gpg.stop()
    gpg.reset_encoders(True)
    sys.exit()

#The Around function will turn the robot to avoid the object in front of it
#The servo will pan and look right and left to take in readings of the
#surroundings so the robot can choose which way to go
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
            digitalWrite(led2,0)
            gpg.turn_degrees(30)
            digitalWrite(led2,1)
            #time.sleep(1)
            print("I am turning right 10 degrees")
        elif rights < lefts and lefts > 15:
            digitalWrite(led1,0)
            gpg.turn_degrees(-30)
            digitalWrite(led1,1)
            #time.sleep(1)
            print("I am turning left 10 degrees")
        elif rights == lefts and rights > 15:
            digitalWrite(led2,0)
            gpg.turn_degrees(30)
            digitalWrite(led2,1)
            #time.sleep(1)
            print("objects equal amount away going right")
        else:
            digitalWrite(led1,0)
            digitalWrite(led2,0)
            digitalWrite(buz,1)
            gpg.drive_cm(-20)
            digitalWrite(buz,0)
            gpg.turn_degrees(90) 
            print("breaking")
            break
        
    return
        
def main():

    try:
        print("GoPiGo3 Autonomous Robot")
        servo.reset_servo()
        time.sleep(1)

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
                camera.capture('/home/pi/Desktop/intheway.jpg')
                Around()
                
                                
            #if there is motion detected the robot will stop then buzz
            #and then will continue throught the code
            elif pir.motion_detected():
                print("motin detected")
                gpg.stop()
                digitalWrite(buz,1)
                print("buzzing")
                time.sleep(.1)
                digitalWrite(buz,0)
                time.sleep(.5)
                
                    

            else:
                gpg.forward()
                digitalWrite(led1,1)
                digitalWrite(led2,1)
        

    except IOError as error:
                print('IO error')
        
    except KeyboardInterrupt:
        print("\nCtrl+C. Exiting.")
        digitalWrite(led1,0)
        digitalWrite(led2,0)
        gpg.stop()
        Exit()

main()
