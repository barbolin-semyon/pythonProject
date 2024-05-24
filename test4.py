import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService


browser = webdriver.Chrome()
URL = " https://qa-course.netlify.app/registration-form-fire"

try:
# Открытие веб-страницы
    browser.get(URL)
# Неявное ожидание для загрузки элементов страницы
    browser.implicitly_wait(5)
# Выбор элемента по имени "firstName"
    input1 = browser.find_element(By.NAME, "firstName")
    input1.send_keys("Semyon")
# Выбор элемента по имени "lastName"
    input2 = browser.find_element(By.NAME, "lastName")
    input2.send_keys("Barbolin")
# Выбор элемента по имени "city"
    input3 = browser.find_element(By.NAME, "city")
    input3.send_keys("Vologda")
# Выбор элемента по имени "email"
    input4 = browser.find_element(By.NAME, "email")
    input4.send_keys("skat.apps@gmail.com")
# Вызов JS-скрипта поиска и нажатия кнопки подтверждения
    script = '''document.querySelector('button[type="submit"]').click();'''
    browser.execute_script(script)

except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
# Задержка перед закрытием браузера
    time.sleep(5)
# закрытие браузера после всех манипуляций
    browser.quit()