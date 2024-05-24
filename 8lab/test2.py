from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver import Chrome

class RabbitPage:
    URL = 'https://qa-test-selectors.netlify.app'
    VARIANT = 3
    HEADING = "Братаны"
    TITLE_TEXT = "На солнышке"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def find_variant(self):
        # Выбор кнопки со 2-ым вариантом, по XPATH
        button = self.browser.find_element(By.XPATH, f'//button[@class="variant__btn"][text()="{self.VARIANT}"]')

        # Нажатие на кнопку с вариантом
        button.click()

    def rabbit_elements_count(self):
        # Поиск элементов с data-type="doggy"
        doggy_elements = self.browser.find_elements(By.XPATH, '//*[@data-type="bunny"]')
        return len(doggy_elements)

    def caught_elements_count(self):
        # Поиск элементов с id="caught"
        caught_elements = self.browser.find_elements(By.ID, 'blackWhite')
        return len(caught_elements)

    def black_elements_count(self):
        # Поиск элементов с class="funnyCat"
        funny_elements = self.browser.find_elements(By.CLASS_NAME, 'blackWhiteRabbit')
        return len(funny_elements)

    def brothers_rabbit_elements_count(self):
        # Поиск элементов с name="pug-dog"
        pug_dog_elements = self.browser.find_elements(By.NAME, 'brothers-rabbits')
        return len(pug_dog_elements)

    def heading_images_count(self):
        # Поиск изображений с heading="Спалился"
        heading_images = self.browser.find_elements(By.XPATH, f'//img[@heading="{self.HEADING}"]')
        return len(heading_images)

    def title_elements_count(self):
        # Поиск элементов с name="smile-dog"
        title_elements = self.browser.find_elements(By.XPATH, f'//h1[text()="{self.TITLE_TEXT}"]')
        return len(title_elements)


# Реализация фикстуры
@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(30)
    yield driver
    driver.quit()

#Функция по проверке осуществления перехода на страницу с вариантом
def test_rabbits_page(browser):
    rabbit_page = RabbitPage(browser)
    rabbit_page.load()
    rabbit_page.find_variant()
    # Реализация проверок с помощью PyTest
    assert rabbit_page.rabbit_elements_count() > 0
    assert rabbit_page.caught_elements_count() > 0
    assert rabbit_page.black_elements_count() > 0
    assert rabbit_page.brothers_rabbit_elements_count() > 0
    assert rabbit_page.heading_images_count() > 0
    assert rabbit_page.title_elements_count() > 0