from selenium import webdriver
import math
import time


link = "http://suninjuly.github.io/alert_accept.html"
stepic = "https://stepik.org/"
stepic_link = "https://stepik.org/lesson/184253/step/4?unit=158843"
login = "a@a.ru"
password = "*****"
browser=webdriver.Chrome()


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


def send_to_stepic(login, password, stepic_link, answer):
	stepic = "https://stepik.org/catalog?auth=login"
	browser.get(stepic)
	browser.find_element_by_name("login").send_keys(login)
	browser.find_element_by_name("password").send_keys(password)
	browser.find_element_by_class_name("sign-form__btn.button_with-loader").click()
	browser.get(stepic_link)
	time.sleep(3)

	browser.find_element_by_css_selector('textarea').send_keys(answer)
	browser.find_element_by_class_name("submit-submission").click()





try:
	#browser=webdriver.Chrome()
	browser.get(link)
	browser.find_element_by_tag_name("button").click()
	browser.switch_to_alert().accept()
	x = browser.find_element_by_id("input_value").text
	y = calc(x)
	input = browser.find_element_by_name("text")
	input.send_keys(y)
	browser.find_element_by_css_selector("button.btn").click()
	alert=browser.switch_to_alert()
	answer = alert.text.split(" ")[-1]
	alert.accept()
	send_to_stepic(login, password, stepic_link, answer)

	
	

except Exception as e:
	print(e)

finally:
	browser.quit()
