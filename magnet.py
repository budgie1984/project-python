import RPi.GPIO as io

io.setmode(io.BCM)

lid_pin = 11  # GPIO 11

#printed = 0


io.setup(lid_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

def isLidOpen():
    return io.input(lid_pin) 


