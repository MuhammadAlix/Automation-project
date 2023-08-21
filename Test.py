import pyautogui
import time

pyautogui.prompt(text ="",title ="Enyer your message")
x, y = pyautogui.locateCenterOnScreen("Up_Button2.jpg", confidence=0.7)
pyautogui.moveTo(x, y, 1)