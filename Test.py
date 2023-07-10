import pyautogui

pyautogui.prompt(text ="",title ="Enyer your message")
x, y = pyautogui.locateCenterOnScreen("Construction.jpg", confidence=0.5)
pyautogui.move(x, y )