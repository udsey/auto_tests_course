import unittest
from selenium import webdriver
import time



def registration_check(link):

    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element_by_xpath("//           div[@class='first_block']//input[@class='form-control first']")
    input_name.send_keys("Ivan")
    input_family_name  = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
    input_family_name.send_keys("Ivanov")
    input_email = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")
    input_email.send_keys("ivan@ivanov.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    return welcome_text




class TestLinks(unittest.TestCase):
    def test_link1(self):
        text_a=registration_check("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", text_a)

    def test_link2(self):
        text_a=registration_check("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", text_a )

if __name__=="__main__":
    unittest.main()

