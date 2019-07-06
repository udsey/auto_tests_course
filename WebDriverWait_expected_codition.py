import send_to_stepic

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

#import send_to_stepic

stepic_link = "https://stepik.org/lesson/181384/step/8?unit=156009"
link = "http://suninjuly.github.io/explicit_wait2.html"

try:

	browser = webdriver.Chrome()
	browser.implicitly_wait(5)
	browser.get(link)
	WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR" ))
	browser.find_element_by_id("book").click()
	x = browser.find_element_by_id("input_value").text
	y = calc(x)
	browser.find_element_by_tag_name("input").send_keys(y)
	button = browser.find_element_by_id("solve")
	button.click()
	
	alert = browser.switch_to_alert()
	answer = alert.text.split()[-1]
	alert.accept()
	send_to_stepic.send_to_stepic(browser=browser,answer=answer, stepic_link=stepic_link)

except Exception as e:
	print(e)


finally:
	browser.quit()
	
	
	
