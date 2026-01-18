'''
https://stepik.org/lesson/138920/step/10?unit=196194
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    url = 'https://suninjuly.github.io/registration1.html'
    success_text = 'Congratulations! You have successfully registered!'
    browser = webdriver.Chrome()
    browser.get(url)

    field_first_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input')
    field_first_name.send_keys("Ivan")
    field_last_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input')
    field_last_name.send_keys("Petrov")
    field_email = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input')
    field_email.send_keys('mail@mail.com')

    # Отправляем заполненную форму
    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert success_text == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()