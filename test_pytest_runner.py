from selenium import webdriver
import time
import pytest



class TestAbs():
    def test_passed(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("input[required].first")
        input1.send_keys("Ivan")

        input2 = browser.find_element_by_css_selector("input[required].second")
        input2.send_keys("Petrov")

        input3 = browser.find_element_by_css_selector("input[required].third")
        input3.send_keys("ys@mail.ru")
        time.sleep(5)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        tt = "Congratulations! You have successfully registered!"
        assert tt == welcome_text, "Should be absolute value of a number"


    def test_failed(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("input[required].first")
        input1.send_keys("Ivan")

        input2 = browser.find_element_by_css_selector("input[required].second")
        input2.send_keys("Petrov")

        input3 = browser.find_element_by_css_selector("input[required].third")
        input3.send_keys("ys@mail.ru")
        time.sleep(5)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        tt = "Congratulations! You have successfully registered!"

        assert tt == welcome_text, "Should be absolute value of a number"

