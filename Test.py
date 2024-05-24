from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService


# Создание экземпляра браузера
driver = webdriver.Chrome()

try:
    #Открытие веб-системы
    driver.get('https://www.youtube.com/')
    # Ждем некоторое время (в данном случае, 5 секунд)
    time.sleep(5)
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    #Закрытие браузера
    driver.quit()