#Joshua Wurtenberg

import pyautogui as gui
import keyboard
import time

# Set failsafe equal to false so that the mouse can reach the corner of the screen
gui.FAILSAFE = False
# Global variable for the link RGB color values 
link_color = (12, 106, 196)

# Global variables for the size of the screen
screenWidth, screenHeight = gui.size()

def mouseIsOverLink(mouseX, mouseY):

    # Check if the pixel the mouse is pointing to matches the correct link color
    mouse_color = gui.pixel(mouseX, mouseY)
    if mouse_color == link_color:
        return True
    else:
        return False
    
def searchScreen():
    for i in range(screenWidth):
        for j in range(screenHeight):
            if keyboard.is_pressed('q'):
                return
            gui.moveTo(i,j)
            if mouseIsOverLink(i, j):
                gui.click()


time.sleep(5)
searchScreen()
