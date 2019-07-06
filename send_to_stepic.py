from selenium import webdriver
import time


def send_to_stepic(browser,stepic_link, answer, login="login", password="password"):
	
	stepic = "https://stepik.org/catalog?auth=login"
	browser.get(stepic)
	browser.implicitly_wait(10)
	browser.find_element_by_name("login").send_keys(login)
	browser.find_element_by_name("password").send_keys(password)
	browser.find_element_by_class_name("sign-form__btn.button_with-loader").click()
	time.sleep(2)
	browser.get(stepic_link)
	browser.find_element_by_css_selector('textarea').send_keys(answer)
	button = browser.find_element_by_class_name("submit-submission")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	time.sleep(1)
	button.click()
