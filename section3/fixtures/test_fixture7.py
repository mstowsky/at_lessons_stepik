import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('language', ['ru', 'en-gb', 'de'])
def test_guest_should_see_login_link(browser, language):
    print(f'Test for language: {language}')
    url = f'http://selenium1py.pythonanywhere.com/{language}/'
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, '#login_link')