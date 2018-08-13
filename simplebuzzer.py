#Simple buzzer code on GrovePi Digital Port 8
#Turns buzzer on for one second then off for one second until
#a Keyboard interrupt

from grovepi import*
import time
import sys


buz = 8

pinMode(buz, "OUTPUT")

while True:
    try:
        digitalWrite(buz,1)
        print("buzzing")
        time.sleep(1)

        digitalWrite(buz,0)
        print("Stop buzzing")
        time.sleep(1)

    except KeyboardInterrupt:
        print("\nCtrl+C. Exiting.")
        digitalWrite(buz,0)
        sys.exit()
    except IOError:
        print("Error")
        
