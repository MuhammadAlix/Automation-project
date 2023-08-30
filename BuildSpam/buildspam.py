# Fist of all you need to pyautogui and for it to work you might need to intall opencv for python
# We need pyautogui to locate buttons in game and then to command cursor to click at those buttons
# Although pyautogui works independent of opencv but we need to use the confidence parameter
import pyautogui
import time

# This part will cause a prompt to appear before program starts search for buttons and clicking them also the number you give in this prompt determines the number of times our loop will run. 
n = pyautogui.prompt(text ="",title ="Enter your message")
n=int(n)
n=n+1

#Locate farm icon on screen 
x, y = pyautogui.locateCenterOnScreen("ScreenShots//Farm.jpg", confidence=0.4)
#Click on farm icon
pyautogui.click(x, y, 1)

# Hold program for 0.5 seconds to give time for transition and possible lag 
time.sleep(0.5)

#Locate Upgrade button on screen 
x, y = pyautogui.locateCenterOnScreen("ScreenShots//Up_Button.jpg", confidence=0.5)
#Click on upgrade button
pyautogui.click(x, y, 1)

#More wait as I have observed this transition takes longer
time.sleep(1.2)

# Applying for loop as following actions need to be performed multiple times.
#Notice that here I used the same variable n that was initialized with the number given in prompt.
for i in range(1, n):

    # Locate and click second upgrade button on screen with sleep time of 1 second.
    x, y = pyautogui.locateCenterOnScreen("ScreenShots//Up_Button2.jpg", confidence=0.7)
    pyautogui.click(x, y, 1)
    time.sleep(1)

    #Locate and click help button on screen with sleep time of 0.5 seconds.
    x, y = pyautogui.locateCenterOnScreen("ScreenShots//Help.jpg", confidence=0.6)
    pyautogui.click(x, y, 1)
    time.sleep(0.5)

    #Locate and click cancel button on screen and sleep for 2.5 seconds.
    x, y = pyautogui.locateCenterOnScreen("ScreenShots//Cancel.jpg", confidence=0.56)
    pyautogui.click(x, y, 1)
    time.sleep(2.5)

    #Locate and click yes button on screen and then sleep for 2 seconds.
    x, y = pyautogui.locateCenterOnScreen("ScreenShots//Yes.jpg", confidence=0.6)
    pyautogui.click(x, y, 1)
    time.sleep(2)

#Please note I have selected these confidence values in locateOnScreen function by repeated trail and error.
#Steam version of lords mobile was used for these tests and I haven't yet tested it with emulators but I think it should work fine with them too with a little tweaks required to be made in confidence values, If that does not work try replacing the images with new screenshots from the game.
#Use Test.py to test working for each button, if the cursor moves slowly towards the desired button then it is working fine, otherwise try tweaking confidence values (0-1) or maybe replace respective screenshot.