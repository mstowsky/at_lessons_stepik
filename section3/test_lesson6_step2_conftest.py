from selenium.webdriver.common.by import By

url = 'http://selenium1py.pythonanywhere.com/'

def test_guest_should_see_login_link(browser):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, "#login_link")