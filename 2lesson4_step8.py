from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"


try:
	browser = webdriver.Chrome()
	browser.maximize_window()
	browser.get(link)
	
	time.sleep(3)
	price = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "$100" )
		)
	button = browser.find_element(By.ID, "book")
	button.click()
	
	x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
	x = x_element.text
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	y = calc(x)
	input = browser.find_element(By.ID, "answer")
	input.send_keys(y)
	button = browser.find_element(By.ID, "solve")
	button.click()
	
finally:
	time.sleep(5)
	browser.quit()
	