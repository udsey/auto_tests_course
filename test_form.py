
from selenium import webdriver
import time

link2 = "http://suninjuly.github.io/registration2.html"
link1 = "http://suninjuly.github.io/registration1.html"

def test_registration_form_test(link):

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
    return welcome_text

"Поздравляем! Вы успешно зарегистировались!", "Oops"


import unittest

class TestLinks(unittest.TestCase):
    def test_link1(self):
        self.assertEqual(test_registration_form_test(link1), "Поздравляем! Вы успешно зарегистировались!" , "oops")

    def test_link2(self):
        self.assertEqual(test_registration_form_test(link2), "Поздравляем! Вы успешно зарегистировались!" , "oops")



if __name__=="__main__":
    unittest.main()

