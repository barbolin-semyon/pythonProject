import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
URL = "https://qa-course.netlify.app/registration-form"
try:
    # Открытие веб-страницы
    browser.get(URL)
    # Явное ожидание для загрузки элементов страницы
    time.sleep(2)
    # Выбор первого встреченного input по тегу
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Semyon")
    # Выбор элемента по имени "lastName"
    input2 = browser.find_element(By.NAME, "lastName")
    input2.send_keys("Barbolin")
    # Выбор третьего элемента, найденного по названию класса "formControl"
    input3 = browser.find_elements(By.CLASS_NAME, "formControl")[2]
    input3.send_keys("Russia")
    # Выбор элемента ввода, найденного по XPath "//input[@name='city']"
    input4 = browser.find_element(By.XPATH,"//input[@name='city']")
    input4.send_keys("Vologda")
    # Явное ожидание для появления кнопки
    time.sleep(5)
    # Выбор элемента, найденного по CSS-селектору 'button[type="submit"]'
    button = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    button.click() # Нажатие кнопки
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Задержка перед закрытием браузера
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()