'''
https://stepik.org/lesson/228249/step/6?unit=200781
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = 'https://suninjuly.github.io/execute_script.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(0.3)

    x_element = browser.find_element(By.ID, 'input_value')
    x_value = x_element.text
    result = calc(x_value)

    button_submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    # browser.execute_script("arguments[0].scrollIntoView(true);", button_submit)
    browser.execute_script("window.scrollBy(0, 100);")
    text_field = browser.find_element(By.ID, 'answer')
    text_field.send_keys(result)
    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()
    robots_radio = browser.find_element(By.ID, 'robotsRule')
    robots_radio.click()

    button_submit.click()

    time.sleep(5)