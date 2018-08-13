import easygopigo3 as easy
import time
import sys

port2 = "AD2"
gpg = easy.EasyGoPiGo3()
pir = gpg.init_motion_sensor(port2)

def main():
    while True:
        try:
        
            if pir.motion_detected():
                print("motion detected")
                time.sleep(1)

            else:
                print("no motion detected")
        except KeyboardInterrupt:
            print("\nCtrl+C. Exiting.")
            sys.exit()
    
main()
