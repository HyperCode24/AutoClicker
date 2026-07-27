# Import everything
import time
import pydirectinput
import keyboard
import ctypes
import pynput
import cv2
import mss
import numpy as np

# Set up image detection and global variables (ChatGPT assistance)
region = {
    "left": 2270,
    "top": 1270,
    "width": 290,
    "height": 73
}
template = cv2.imread("text screenshot.png", cv2.IMREAD_GRAYSCALE)
template_width = template.shape[1]
template_height = template.shape[0]

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

# Detect when a fish is caught and reel in automatically (ChatGPT assistance)
def fishingSubtitle(tolerance):
    with mss.mss() as sct:
        screenshot = np.array(sct.grab(region))
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(
        gray,
        template,
        cv2.TM_CCOEFF_NORMED
    )
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    print(max_val)
    if max_val > tolerance:
        return True
    else:
        return False

# Waits until a key is pressed and then released
def waitForSubtitle(key):
    print("Waiting for subtitle disappearance and then appearance.")
    while fishingSubtitle(0.9):
        time.sleep(0.1)
    while not(fishingSubtitle(0.9)):
        time.sleep(0.1)
    print("Subtitle appeared.")

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
    '''cursor = ctypes.wintypes.POINT()
    mousePos = ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
    '''
    mouse = pynput.mouse.Controller()
    mousePos = mouse.position
    print("Position is: " + str(mousePos))
    return mousePos

# Move the mouse to any monitor
def globalMouseMove(pos):
    '''ctypes.windll.user32.SetCursorPos(pos)'''
    mouse = pynput.mouse.Controller()
    x, y = pos
    mouse.position = (x,y)

# Automatically switches screens to allow multitasking while fishing
def ac_Fishing():
    waitForSubtitle('v')
    savedSpot = globalMousePos()
    altTab()
    pydirectinput.rightClick()
    stdDelay()
    pydirectinput.rightClick()
    stdDelay()
    altTab()
    globalMouseMove(savedSpot)

# Makes sure failsafes are active
setupFailsafes()

# Run the autocliker infinitely after a short delay for setup
waitsec = 10
cursec = 0
while cursec < waitsec:
    print("Starting in " + str(waitsec-cursec) + " seconds.")
    cursec = cursec + 1
    time.sleep(1)
print("Active")
while True:
    ac_Fishing()