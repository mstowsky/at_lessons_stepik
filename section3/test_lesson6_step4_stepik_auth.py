'''
https://stepik.org/lesson/237240/step/4?unit=209628
'''

import os
import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

url = 'https://stepik.org/lesson/236895/step/1'

def test_stepik_authorizer(browser):
    browser.get(url)

    # Ждем загрузки страницы до появления кнопки авторизации
    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#ember499')))

    login_button = browser.find_element(By.CSS_SELECTOR, '#ember499')
    login_button.click()
    time.sleep(0.5)
    email_input = browser.find_element(By.CSS_SELECTOR, '#id_login_email')
    email_input.send_keys(os.getenv('LOGIN'))
    password_input = browser.find_element(By.CSS_SELECTOR, '#id_login_password')
    password_input.send_keys(os.getenv('PASSWORD'))
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type=submit]')
    submit_button.click()

    # Ждем загрузки страницы после авторизации
    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.navbar__profile-img')))

    time.sleep(3)