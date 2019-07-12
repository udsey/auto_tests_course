import pytest
from selenium import webdriver
import time
import math

links = [
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"
]

@pytest.fixture(scope="function")
def answer():
    return str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()



@pytest.mark.parametrize("link", links)
def test_current_answer(browser, link):
    browser.get(link)
    browser.get(link)
    browser.find_element_by_tag_name("textarea").send_keys(answer)
    browser.find_element_by_class_name("submit-submission ").click()
    x = browser.find_element_by_class_name("smart-hints__hint").text
    assert x == "Correct!"




