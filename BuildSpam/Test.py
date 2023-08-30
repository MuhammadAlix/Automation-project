import pyautogui
import time

pyautogui.prompt(text ="",title ="Enyer your message")
x, y = pyautogui.locateCenterOnScreen("Cancel.jpg", confidence=0.56)
pyautogui.moveTo(x, y, 1)