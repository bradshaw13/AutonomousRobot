import easygopigo3 as easy
import time
import sys

gpg = easy.EasyGoPiGo3()

print("Emergency Stop")

gpg.stop()

sys.exit
