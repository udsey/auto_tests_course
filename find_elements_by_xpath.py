from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)


elements = browser.find_elements_by_class_name("first_block").find_elements_by_class_name()



browser.find_elements_by_xpath("//form/div[1]//input[contains(@class, 'form-group first_class') and contains(@class, 'form-control second')and contains(@class, 'form-control third')]")

for element in elements:
	element.send_keys("Answer")
	time.sleep(0.1)

button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(1)

welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

browser.quit()





