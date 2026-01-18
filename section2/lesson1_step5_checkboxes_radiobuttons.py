'''
https://stepik.org/lesson/165493/step/5?unit=140087
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(0.3)

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x_value = x_element.text
result = calc(x_value)

text_element = browser.find_element(By.CSS_SELECTOR, '#answer')
text_element.send_keys(result)

checkbox_element = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
checkbox_element.click()

radio_element = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
radio_element.click()

button_submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
button_submit.click()

time.sleep(5)
browser.quit()