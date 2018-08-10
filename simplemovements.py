#This code is going to make the robot move in simple directions
#and going forward
#Author: Alexander Bradshaw

import easygopigo3 as easy
import time
import sys



gpg = easy.EasyGoPiGo3()

gpg.forward()
time.sleep(5)
gpg.left()
time.sleep(2)
gpg.forward()
time.sleep(2)
gpg.stop()

gpg.drive_inches(12, True)
gpg.stop()

sys.exit
