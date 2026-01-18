'''
https://stepik.org/lesson/228249/step/3?unit=200781
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

url = 'https://suninjuly.github.io/selects1.html'
# url = 'https://suninjuly.github.io/selects2.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(0.3)

    num1_value = browser.find_element(By.ID, 'num1').text
    num2_value = browser.find_element(By.ID, 'num2').text
    summ_result = int(num1_value)+int(num2_value)
    result_field = browser.find_element(By.ID, 'dropdown')
    select = Select(result_field)
    select.select_by_value(str(summ_result))

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    time.sleep(5)