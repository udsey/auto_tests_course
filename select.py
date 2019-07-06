from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link="http://suninjuly.github.io/selects1.html"

try:
	browser=webdriver.Chrome()
	browser.get(link)
	x = browser.find_element_by_id("num1").text
	y = browser.find_element_by_id("num2").text
	z = str(int(x)+int(y))
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(z)
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	alert=browser.switch_to_alert()
	print(alert.text)

except Exception as e:
	print(e)

finally:
	browser.quit()

	
	
