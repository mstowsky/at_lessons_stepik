'''
https://stepik.org/lesson/184253/step/6?unit=158843
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = 'https://suninjuly.github.io/redirect_accept.html'

with webdriver.Chrome() as browser:
    browser.get(url)

    button_submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button_submit.click()

    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element(By.ID, 'input_value')
    x_value = x_element.text
    result = calc(x_value)
    result_field = browser.find_element(By.ID, 'answer')
    result_field.send_keys(result)
    button_submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button_submit.click()

    time.sleep(5)