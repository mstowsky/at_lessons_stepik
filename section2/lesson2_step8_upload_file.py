'''
https://stepik.org/lesson/228249/step/8?unit=200781
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

url = 'https://suninjuly.github.io/file_input.html'
filename = 'input.txt'
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, filename)

with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(0.3)

    first_name_field = browser.find_element(By.NAME, 'firstname')
    first_name_field.send_keys('Ivan')
    last_name_field = browser.find_element(By.NAME, 'lastname')
    last_name_field.send_keys('Petrov')
    email_field = browser.find_element(By.NAME, 'email')
    email_field.send_keys('mail@mail.com')

    file_field = browser.find_element(By.ID, 'file')
    file_field.send_keys(file_path)

    button_submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button_submit.click()
    time.sleep(3)