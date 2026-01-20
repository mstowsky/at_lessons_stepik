import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def browser():
    print('\n--- Open browser ---')
    browser = webdriver.Chrome()
    yield browser
    print("\n--- Close browser ---")
    browser.quit()