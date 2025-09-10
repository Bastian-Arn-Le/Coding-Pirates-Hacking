import pyautogui
import time

time.sleep(2)

pyautogui.press("win")
time.sleep(1)
pyautogui.typewrite("cmd")
pyautogui.press("enter")
time.sleep(3) 

pyautogui.press("enter")
time.sleep(0.5)

pyautogui.typewrite('reg add "HKCU\\Control Panel\\Desktop" /v Wallpaper /t REG_SZ /d "C:\\Users\\basti\\Pictures\\jens.png" /f')
pyautogui.press("enter")
time.sleep(1)

pyautogui.typewrite('RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters')
pyautogui.press("enter")
