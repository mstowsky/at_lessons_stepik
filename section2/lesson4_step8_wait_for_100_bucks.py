'''
https://stepik.org/lesson/181384/step/8?unit=156009
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = 'https://suninjuly.github.io/explicit_wait2.html'

with webdriver.Chrome() as browser:
    browser.get(url)

    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'),"$100"))
    button_submit = browser.find_element(By.ID, 'book')
    button_submit.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x_value = x_element.text
    result = calc(x_value)
    result_field = browser.find_element(By.ID, 'answer')
    result_field.send_keys(result)
    button_submit = browser.find_element(By.ID, 'solve')
    button_submit.click()

    time.sleep(15)