import pyautogui
import time

pyautogui.prompt(text ="",title ="Enyer your message")

x, y = pyautogui.locateCenterOnScreen("Events.jpg", confidence=0.3)
pyautogui.click(x, y, 1)

time.sleep(2)

guildfest=pyautogui.locateCenterOnScreen("Guildfest.jpg", confidence=0.4)
# print(guildfest, type(guildfest))

# if guildfest == 'None':
#     pyautogui.scroll(10, x=100, y=100)
#     guildfest=pyautogui.locateCenterOnScreen("Guildfest.jpg", confidence=0.6)

x, y = guildfest
pyautogui.click(x, y, 1)   

