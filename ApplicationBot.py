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
    # Locate the application button and click it
    time.sleep(1)
    applicationButton = gui.locateCenterOnScreen('easy_apply.png')
    gui.moveTo(applicationButton)
    gui.click()
    time.sleep(1)

    # Click through the prompts
    while gui.locateCenterOnScreen('next_button.png'):
        gui.click(gui.locateCenterOnScreen('next_button.png'))
        time.sleep(1)

        # Check for any missing info (exit and save application if missing info)
        if gui.locateCenterOnScreen('stop.png'):
            gui.click(gui.locateCenterOnScreen('exit_popup.png'))
            time.sleep(1)
            gui.click(gui.locateCenterOnScreen('save.png'))
            return
    time.sleep(1)
    gui.click(gui.locateCenterOnScreen('review_button.png'))
    time.sleep(1)
    if gui.locateCenterOnScreen('stop.png'):
            gui.click(gui.locateCenterOnScreen('exit_popup.png'))
            time.sleep(1)
            gui.click(gui.locateCenterOnScreen('save.png'))
            return
    gui.click(gui.locateCenterOnScreen('submit_application.png'))
    time.sleep(1)
    gui.click(gui.locateCenterOnScreen('exit_popup.png'))

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
    keepgoing = True
    while keepgoing:

        # Moves the cursor down 5 pixels at a time
        for i in range(260, screenHeight - 50, 5):
            if keyboard.is_pressed('q'):
                return
            gui.moveTo(480, i)
            if mouseIsOverJob(480, i):
                gui.click()
                apply()
        gui.scroll(-1000)


# Opening FireFox
print("Press 'q' to stop program!")
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
apply()
searchList()

