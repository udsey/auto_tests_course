from selenium import webdriver
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
	browser=webdriver.Chrome()
	browser.get(link)
	x=browser.find_element_by_id("input_value").text
	y=calc(x)
	input=browser.find_element_by_id("answer")
	input.send_keys(y)
	button=browser.find_element_by_css_selector("button.btn")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	browser.find_element_by_css_selector("[for='robotCheckbox']").click()
	browser.find_element_by_css_selector("[for='robotsRule']").click()
	button.click()
	alert=browser.switch_to_alert()
	print(alert.text)

except Exeption as e:
	print(e)

finally:
	browser.quit()