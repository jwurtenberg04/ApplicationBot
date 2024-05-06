#Joshua Wurtenberg

import pyautogui as gui
import keyboard
import time

# Code to print mouse position to the terminal for testing purposes
def getMousePos():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = gui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

def getMouseColor():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = gui.position()
            mouseColor = gui.pixel(x, y)
            print(mouseColor)
    except KeyboardInterrupt:
        print('\n')

def apply():
    applicationButton = gui.locateCenterOnScreen('easy_apply.png')
    gui.moveTo(applicationButton)
    gui.click()
# Set failsafe equal to false so that the mouse can reach the corner of the screen
gui.FAILSAFE = False
# Global variable for the link RGB color values 
light_blue = (10, 102, 194)
white = (255, 255, 255)
# Global variables for the size of the screen
screenWidth, screenHeight = gui.size()

# Edit these variables according to your need
jobTitle = "Software Engineering"
location = "Fort Myers"

def mouseIsOverJob(mouseX, mouseY):

    # Check if the pixel the mouse is pointing to matches the correct color for an unselected job posting
    mouse_color = gui.pixel(mouseX, mouseY)
    if mouse_color == white:
        return True
    else:
        return False
    
def searchList():
    for i in range(260, screenHeight, 10):
        if keyboard.is_pressed('q'):
            return
        gui.moveTo(480, i)
        if mouseIsOverJob(480, i):
            gui.click()
            apply()

# Opening FireFox
gui.press("win")
time.sleep(1)
gui.write("FireFox")
time.sleep(1)
gui.press('enter')
time.sleep(2)

# Navigating to LinkedIn website
gui.click(400, 65)
gui.write("https://www.linkedin.com")
gui.press('enter')
time.sleep(5)

# Search for jobs in your field and area
gui.click(1015, 126)
time.sleep(2)
gui.click(696, 109)
gui.write(location)
gui.click(528, 113)
gui.write(jobTitle)
gui.press('enter')
time.sleep(5)
gui.click(1262, 163)
time.sleep(3)
gui.click(900, 156)
time.sleep(2)
gui.click(778, 222)
time.sleep(2)
gui.click(778, 263)
time.sleep(2)
gui.click(984, 494)
time.sleep(5)

searchList()

