from selenium import webdriver
import os



try:
	link = "http://suninjuly.github.io/file_input.html"
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, "file.txt")
	browser = webdriver.Chrome()
	browser.get(link)
	elements = browser.find_elements_by_xpath("//label[contains(text(), '*')]/following::input[1]")
	for element in elements:
		element.send_keys("Answer")
	
	input_but = browser.find_element_by_id("file")
	input_but.send_keys(file_path)
	browser.find_element_by_css_selector("button.btn").click()
	alert=browser.switch_to_alert().text
	print(alert)

except Exception as e:
	print(e)

finally:
	browser.quit()
	
