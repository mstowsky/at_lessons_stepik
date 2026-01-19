'''
https://stepik.org/lesson/36285/step/13?unit=162401
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

url1 = 'http://suninjuly.github.io/registration1.html'
url2 = 'https://suninjuly.github.io/registration2.html'
welcome_text_expected = 'Congratulations! You have successfully registered!'

class RegistrationTest(unittest.TestCase):
    def test_registration_page1(self):
        with webdriver.Chrome() as browser:
            browser.get(url1)

            # Заполняем обязательные поля формы
            first_name_field = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input')
            first_name_field.send_keys("Ivan")
            last_name_field = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input')
            last_name_field.send_keys("Petrov")
            email_field = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input')
            email_field.send_keys('mail@mail.com')
            submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            submit_button.click()
            time.sleep(1)
            welcome_text_actual = browser.find_element(By.TAG_NAME, 'h1').text

            # Сравниваем полученный итоговый текст с ожидаемым
            self.assertEqual(welcome_text_expected, welcome_text_actual, f'Test failed. Expected {welcome_text_expected}, but got {welcome_text_actual}')

            time.sleep(3)

    def test_registration_page2(self):
        with webdriver.Chrome() as browser:
            browser.get(url2)

            # Заполняем обязательные поля формы
            first_name_field = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input')
            first_name_field.send_keys("Ivan")
            last_name_field = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input')
            last_name_field.send_keys("Petrov")
            email_field = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input')
            email_field.send_keys('mail@mail.com')
            submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            submit_button.click()
            time.sleep(1)
            welcome_text_actual = browser.find_element(By.TAG_NAME, 'h1').text

            # Сравниваем полученный итоговый текст с ожидаемым
            self.assertEqual(welcome_text_expected, welcome_text_actual, f'Test failed. Expected {welcome_text_expected}, but got {welcome_text_actual}')

            time.sleep(3)