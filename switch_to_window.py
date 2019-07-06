from selenium import webdriver
import math
import send_to_stepic

link="http://suninjuly.github.io/redirect_accept.html"

stepic_link = "https://stepik.org/lesson/184253/step/6?unit=158843"


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
	browser = webdriver.Chrome()
	browser.implicitly_wait(5)
	browser.get(link)
	browser.find_element_by_css_selector("button[type='submit']").click()
	new_window = browser.window_handles[1]
	browser.close()
	browser.switch_to_window(new_window)
	x = browser.find_element_by_id("input_value").text
	y = calc(x)
	browser.find_element_by_id("answer").send_keys(y)
	browser.find_element_by_css_selector("button.btn").click()
	alert = browser.switch_to_alert()
	answer = alert.text.split()[-1]
	alert.accept()
	send_to_stepic.send_to_stepic(browser=browser,answer=answer, stepic_link=stepic_link)

except Exception as e:
	print(e)

finally:
	browser.quit()

	
