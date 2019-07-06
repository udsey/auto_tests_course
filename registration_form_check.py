from selenium import webdriver
import time

#link = "http://suninjuly.github.io/registration2.html"
link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()

    browser.get(link)

    input_name = browser.find_element_by_xpath("//           div[@class='first_block']//input[@class='form-control first']")
    input_family_name  = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
    input_email = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")


    input_name.send_keys("Ivan")
    input_family_name.send_keys("Ivanov")
    input_email.send_keys("ivan@ivanov.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

except Exception as e:
    print(e)

finally:
    browser.quit()
