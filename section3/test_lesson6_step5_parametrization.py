'''
https://stepik.org/lesson/237240/step/5
'''

import time
import math
import pytest
from dotenv import load_dotenv
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

load_dotenv()

def stepik_answer():
    return math.log(int(time.time()))

list_of_pages = ['https://stepik.org/lesson/236895/step/1',
                'https://stepik.org/lesson/236896/step/1',
                'https://stepik.org/lesson/236897/step/1',
                'https://stepik.org/lesson/236898/step/1',
                'https://stepik.org/lesson/236899/step/1',
                'https://stepik.org/lesson/236903/step/1',
                'https://stepik.org/lesson/236904/step/1',
                'https://stepik.org/lesson/236905/step/1']

expected_text = 'Correct!'
message_words = []

@pytest.fixture(scope="session", autouse=True)
def print_final_message():
    """Фикстура, которая выполняется после всех тестов."""
    yield
    print('Stepik\'s hidden message is: ', *message_words, sep='')

@pytest.mark.parametrize('page_link', list_of_pages)
def test_stepik_open_different_pages(auth, page_link):
    print(f'Test for page: {page_link}')
    browser = auth
    browser.get(page_link)
    time.sleep(5)

    # Если есть кнопка "Решить снова", то нажимаем, иначе ничего не делаем.
    try:
        again_button = browser.find_element(By.CSS_SELECTOR, '.again-btn')
        again_button.click()
        time.sleep(2)
    except NoSuchElementException:
        pass

    answer_input = browser.find_element(By.CSS_SELECTOR, '.textarea')
    # Без "активации" поля через JavaScript значение никак не хотелось вводиться.
    browser.execute_script("arguments[0].focus();", answer_input)
    answer_input.send_keys(str(stepik_answer()))

    answer_button = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    answer_button.click()
    time.sleep(3)
    result_text_actual = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    try:
        assert expected_text == result_text_actual, f'Error. Expected \'{expected_text}\', but got \'{result_text_actual}\'.'
    except AssertionError as e:
        print(f'Result text is: \'{result_text_actual}\'')
        message_words.append(result_text_actual)
        raise e