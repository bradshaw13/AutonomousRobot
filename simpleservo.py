#Simple code to get familiar with how the servo rotates and will take in sensor
#readings
#Author: Alexander Bradshaw

import easygopigo3 as easy
import time
import sys



gpg = easy.EasyGoPiGo3()


servo = gpg.init_servo("SERVO1")
uss = gpg.init_ultrasonic_sensor()

add = 180
num = 0
while True:
    servo.rotate_servo(90)
    lefts = uss.read()
    break
print(" Left side value = ", lefts)

    
    

#for i in range(4):
 #   if i % 2 == 0:
  #      servo.rotate_servo(num+add)
   # else:
    #    servo.rotate_servo(num-add)
    
#servo.reset_servo()

#servo.rotate_servo(180)



#time.sleep(1)
#servo.rotate_servo(60)

servo.reset_servo()
 




print("hi")

sys.exit()
