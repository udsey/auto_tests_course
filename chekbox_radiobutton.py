from selenium import webdriver
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link="http://suninjuly.github.io/get_attribute.html"

try:
	browser=webdriver.Chrome()
	browser.get(link)
	img=browser.find_element_by_tag_name('img')
	x=img.get_attribute("valuex")
	y=calc(x)
	input=browser.find_element_by_tag_name('input')
	input.send_keys(y)
	checkbox=browser.find_element_by_id("robotCheckbox")
	checkbox.click()
	radiobutton=browser.find_element_by_id("robotsRule")
	radiobutton.click()
	button=browser.find_element_by_css_selector("button.btn")
	button.click()
	alert=browser.switch_to_alert()
	print(alert.text)

except Exeption as e:
	print(e)

finally:
	browser.quit()


