import time
import myemail
import RPi.GPIO as io

io.setmode(io.BCM)

door_pin = 11  # GPIO 11

printed = 0
#loop = 1

io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

def isLidOpen():

    return io.input(door_pin) 

