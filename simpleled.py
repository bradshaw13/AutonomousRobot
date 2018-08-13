#Simple testing on GrovePi
#with two led lights, Blue led on Digitial Port 3
#Red led on Digital Port 2
#
#
#Author: Alexander Bradshaw

import time
import sys
from grovepi import*

#Initializes ports and pinMode for each of the led lights
led1 = 3
pinMode(led1, "OUTPUT")
#time.sleep(.5)

led2 = 2
pinMode(led2, "OUTPUT")
#time.sleep(.5)


#Alternates between turning on the blue led and red led

while True:
    try:
        digitalWrite(led1,1)
        digitalWrite(led2,0)
        print("Blue Light is on!")
        time.sleep(1)
        digitalWrite(led1,0)
        digitalWrite(led2,1)
        print("Red light is on")
        time.sleep(1)

    except KeyboardInterrupt:
        digitalWrite(led1,0)
        digitalWrite(led2,0)
        sys.exit()
    except IOError:
        print("Error")
