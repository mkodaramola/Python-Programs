from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from langdetect import detect
# # import pyautogui as pg
import re
from bs4 import BeautifulSoup


def bingSearch(t):
	driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
	#driver.maximize_window()
	driver.get("https://www.bing.com/")
	time.sleep(0.3)
	searchBox = driver.find_element_by_xpath("//input[@id='sb_form_q']")
	searchBox.click()
	action = ActionChains(driver)
	searchBox.send_keys(t)
	time.sleep(0.3)
	searchBox.submit()
	si = 6
	res1 = driver.find_element_by_xpath(f"//h2[{si-5}]/a[1]")
	resPage = driver.find_element_by_xpath(f"//ol[@id='b_results']/li[@class='b_algo']/div[@class='b_caption']/div[@class='b_attribution']/cite[1]")


	if "image" in res1.text.lower():
		pass
	else:

		
		driver.get(resPage.text)
		#time.sleep(5)
		# driver.execute_script("window.stop();")

		txt = driver.page_source

		# clean = re.compile('<script.*?script>')
		# t = re.sub(clean,'',t)

		# clean = re.compile('<style.*?style>')
		# t = re.sub(clean,'',t)

		# clean = re.compile('<.*?>')
		# t = re.sub(clean,'',t)

		# clean = re.compile('{.*?}')
		# t = re.sub(clean,'',t)
		soup = BeautifulSoup(txt)
		txt = soup.get_text()

		

		txt = txt.encode('utf-8').decode('ascii', 'ignore')
		p = t+" is"
		txt = txt.lower() 
		if no_of_words(t) == 1 and p in txt:
			pos = txt.find(p)
			txt = txt[pos:len(txt)]


		print(txt)
		f = open('pageC.txt','w')
		f.write(str(txt))
		f.close()


def no_of_words(t):
	t = t.strip()
	count = 0
	for i in range(len(t)):
		if i == " ":
			count +=1

	return count+1

print(bingSearch("Theophilus Sunday latest songs"))




