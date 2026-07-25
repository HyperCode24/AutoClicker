import time

import pydirectinput
import keyboard

# Sets the failsafe delay while keeping the corner breakout
def setupFailsafes():
    pydirectinput.FAILSAFE = True
    pydirectinput.PAUSE = 0

# Waits until a key is pressed and then released
def waitForKey(key):
    print("Waiting for " + key + " key press.")
    while not(keyboard.is_pressed(key)):
        time.sleep(0.1)
    while keyboard.is_pressed(key):
        time.sleep(0.1)
    print(key + " key pressed and released.")

# Define the delay your computer needs to register different keys here
def stdDelay():
    time.sleep(0.1)

# Alt tabs
def altTab():
    pydirectinput.keyDown("alt")
    pydirectinput.keyDown("tab")
    pydirectinput.keyUp("tab")
    pydirectinput.keyUp("alt")
    stdDelay()

# Report the mouse position
def globalMousePos():
    return pydirectinput.position()

# Automatically switches screens to allow multitasking while fishing
def ac_Fishing():
    waitForKey('v')
    savedSpot = globalMousePos()
    altTab()
    pydirectinput.rightClick()
    stdDelay()
    pydirectinput.rightClick()
    stdDelay()
    altTab()
    pydirectinput.moveTo(savedSpot)

# Makes sure failsafes are active
setupFailsafes()

# Run the autocliker infinitely
while True:
    ac_Fishing()

