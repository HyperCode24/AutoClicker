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
template = cv2.imread("text screenshot.png", cv2.IMREAD_GRAYSCALE)
template_width = template.shape[1]
template_height = template.shape[0]

# Sets the failsafe delay while keeping the corner breakout
def setupFailsafes():
    pydirectinput.FAILSAFE = True
    pydirectinput.PAUSE = 0

# Reports if the key is pressed
def keyPressed(key):
    return keyboard.is_pressed(key)

# Waits until a key is pressed and then released
def waitForKey(key):
    print("Waiting for " + key + " key press.")
    while not(keyboard.is_pressed(key)):
        time.sleep(0.1)
    while keyboard.is_pressed(key):
        time.sleep(0.1)
    print(key + " key pressed and released.")

# Detect when a fish is caught and reel in automatically (ChatGPT assistance)
def fishingSubtitle(box,tolerance):
    with mss.MSS() as sct:
        screenshot = np.array(sct.grab(box))
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(
        gray,
        template,
        cv2.TM_CCOEFF_NORMED
    )
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    #a sprint(max_val)
    if max_val > tolerance:
        return True
    else:
        return False

# Waits until a key is pressed and then released
def waitForSubtitle(box,tolerance):
    #print("Waiting for subtitle disappearance and then appearance.")
    while fishingSubtitle(box,tolerance):
        time.sleep(0.1)
    while not(fishingSubtitle(box,tolerance)):
        time.sleep(0.1)
    #print("Subtitle appeared.")

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
def globalMousePos(debug=False):
    '''cursor = ctypes.wintypes.POINT()
    mousePos = ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
    '''
    mouse = pynput.mouse.Controller()
    mousePos = mouse.position
    if debug:
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
    region = {
        "left": 2270,
        "top": 1270,
        "width": 290,
        "height": 73
    }
    waitForSubtitle(region,0.8)
    savedSpot = globalMousePos()
    altTab()
    pydirectinput.rightClick()
    stdDelay()
    pydirectinput.rightClick()
    stdDelay()
    altTab()
    globalMouseMove(savedSpot)

# Fishing for only one screen
def ac_Fishing2():
    region = {
        "left": -291,
        "top": 1277,
        "width": 290,
        "height": 65
    }
    waitForSubtitle(region,0.8)
    pydirectinput.rightClick()
    stdDelay()
    pydirectinput.rightClick()
    stdDelay()

# Show where the mouse is
def debug_mousePos():
    while not (keyPressed('v')):
        globalMousePos(True)

# Makes sure failsafes are active
setupFailsafes()

# Short delay for setup
waitsec = 5
cursec = 0
while cursec < waitsec:
    print("Starting in " + str(waitsec-cursec) + " seconds.")
    cursec = cursec + 1
    time.sleep(1)
print("Active")

# Run the autocliker infinitely and report times ran
operations = 0
totalStart = time.time()
while True:
    operationStart = time.time()
    
    # The actual operation to perform
    ac_Fishing2()
    
    operationDone = time.time()
    totalDone = time.time()
    totalElapsed = round(totalDone - totalStart,2)
    operationElapsed = round(operationDone - operationStart,2)
    operations = operations + 1
    print("Completed operation " + str(operations) + " in " + str(operationElapsed) + "s. Total time elapsed: " + str(totalElapsed) + "s.")

# Otherwise run debug mouse position code
debug_mousePos()