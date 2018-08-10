#Simple readings with the Ultrasonic sensor to get familiar with it
#Author: Alexander Bradshaw

import easygopigo3 as easy
import time
import sys


port1 = "AD1"

gpg = easy.EasyGoPiGo3()

uss = gpg.init_ultrasonic_sensor(port1)

while True:
    try:
        print("Ultrasonic Reaading", uss.read()) 

    except KeyboardInterrupt:
        sys.exit
