'''
https://stepik.org/lesson/138920/step/8?unit=196194
'''

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

url = 'https://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys('Ivan')
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys('Petrov')
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys('Smolensk')
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//html/body/div/form/div/button[@type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()