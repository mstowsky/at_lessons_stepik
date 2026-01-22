import os
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

stepik_login_url = 'https://stepik.org/catalog?auth=login'

@pytest.fixture(scope='session')
def browser():
    print('\n--- Open browser ---')
    browser = webdriver.Chrome()
    yield browser
    print("\n--- Close browser ---")
    browser.quit()

@pytest.fixture(scope='session')
def auth(browser):
    print('\n--- Authorization ---')
    browser.get(stepik_login_url)

    # Ждем загрузку формы авторизации
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'ember1558')))

    # Заполняем логин и пароль, нажимаем "Войти"
    browser.find_element(By.ID, 'id_login_email').send_keys(os.getenv('LOGIN'))
    browser.find_element(By.ID, 'id_login_password').send_keys(os.getenv('PASSWORD'))
    browser.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

    # Ожидание и проверка успешной авторизации
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "navbar__profile-img")))

    print('\n--- Authorization is successful ---')
    return browser