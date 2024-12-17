from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import keyboard
from threading import Thread







def ResponsiveClick(x,y):
	rsw = 1366
	rsh = 768
	scrWidth,scrHeight=pyautogui.size()
	nx = (scrWidth * x)//1366
	ny = (scrHeight * y)//768
	pyautogui.click(nx,ny)

def myDrag(x,y):
	rsw = 1366
	rsh = 768
	scrWidth,scrHeight=pyautogui.size()
	nx = (scrWidth * x)//1366
	ny = (scrHeight * y)//768
	pyautogui.dragTo(nx,ny)


def getText():
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get("C:\\Users\\user\\Documents\\Programming\\www.w3schools.com\\index.html")
	html = driver.find_element_by_link_text("LEARN HTML")
	html.click()

	sleep(2)

	ResponsiveClick(1054,416)
	sleep(2)

	ResponsiveClick(239,500)

	myDrag(684,680)

	pyautogui.hotkey("ctrl","c")

	os.startfile("db.txt")
	sleep(0.2)
	pyautogui.hotkey("ctrl","v")


def disableKeys():
	for i in range(150):
		keyboard.block_key(i)


t1 = Thread(target=disableKeys)
t2 = Thread(target=getText)

t1.start()
t2.start()



# p1 = driver.find_element_by_xpath("//div[@class='tutintro']/p[1]")

# print(p1.text)