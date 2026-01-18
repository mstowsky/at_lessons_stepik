'''
https://stepik.org/lesson/165493/step/7?unit=140087
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = 'https://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(0.3)

x_element = browser.find_element(By.ID, 'treasure')
x_value = x_element.get_attribute('valuex')
result = calc(x_value)

text_field = browser.find_element(By.ID, 'answer')
text_field.send_keys(result)

robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
robot_checkbox.click()

robots_radio = browser.find_element(By.ID, 'robotsRule')
robots_radio.click()

button_submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
button_submit.click()

time.sleep(3)
browser.quit()