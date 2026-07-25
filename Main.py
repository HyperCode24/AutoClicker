import pydirectinput
import keyboard

# Sets the failsafe delay while keeping the corner breakout
def setupFailsafes():
    pydirectinput.FAILSAFE = True
    pydirectinput.PAUSE = 1

# Makes sure failsafes are active
setupFailsafes()

while True:
    if keyboard.is_pressed('n'):
        print("N key pressed")
    else:
        print("Key not down")
