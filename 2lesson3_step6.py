from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"


try:
	browser = webdriver.Chrome()
	browser.maximize_window()
	browser.get(link)
	
	time.sleep(3)
	button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
	button.click()
	
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	
	x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
	x = x_element.text
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	y = calc(x)
	input = browser.find_element(By.ID, "answer")
	input.send_keys(y)
	button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
	button.click()
	
finally:
	time.sleep(10)
	browser.quit()
	