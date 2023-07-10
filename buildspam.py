import pyautogui
import time

n = pyautogui.prompt(text ="",title ="Enyer your message")
n=int(n)
x, y = pyautogui.locateCenterOnScreen("Farm.jpg", confidence=0.5)
pyautogui.click(x, y, 1)

time.sleep(0.5)

x, y = pyautogui.locateCenterOnScreen("Up_Button.jpg", confidence=0.5)
pyautogui.click(x, y, 1)

time.sleep(0.5)
for i in range(1, n):
    x, y = pyautogui.locateCenterOnScreen("Up_Button2.jpg", confidence=0.6)
    pyautogui.click(x, y, 1)

    time.sleep(0.5)

    x, y = pyautogui.locateCenterOnScreen("Help.jpg", confidence=0.6)
    pyautogui.click(x, y, 1)

    time.sleep(0.5)

    x, y = pyautogui.locateCenterOnScreen("Cancel.jpg", confidence=0.5)
    pyautogui.click(x, y, 1)

    time.sleep(2)

    x, y = pyautogui.locateCenterOnScreen("Yes.jpg", confidence=0.6)
    pyautogui.click(x, y, 1)
    time.sleep(1)