from selenium import webdriver

browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_xpath_form")
input1= browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("form-control.city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")

xpath="//div/button[contains(text(), 'Отправить')]"
button = browser.find_element_by_xpath(xpath)
button.click()

alert=browser.switch_to_alert()
print(alert.text)
browser.quit()


