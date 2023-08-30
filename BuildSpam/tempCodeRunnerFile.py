import pyautogui
pyautogui.prompt(text ="",title ="Enyer your message")
guildfest=pyautogui.locateCenterOnScreen("Guildfest.jpg", confidence=0.6)
print(guildfest, type(guildfest))
x, y = guildfest
pyautogui.click(x, y)