from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

xpath= "//label[contains(text(), '*')]/following::input[1]"
elements = browser.find_elements_by_xpath(xpath)

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





