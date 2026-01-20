'''
https://stepik.org/lesson/237240/step/4?unit=209628
'''

from selenium.webdriver.common.by import By

url = 'https://stepik.org/lesson/236895/step/1'

def stepik_authorizer(browser):
    browser.get(url)