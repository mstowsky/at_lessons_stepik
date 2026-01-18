'''
https://stepik.org/lesson/138920/step/7?unit=196194
'''

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

url = 'https://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys('Answer')
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    time.sleep(5)
    browser.quit()