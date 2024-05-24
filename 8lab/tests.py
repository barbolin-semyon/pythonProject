import pytest
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By


class DuckDuckGoSearchPage:
    URL = 'https://www.duckduckgo.com'
    SEARCH_INPUT = (By.ID, "searchbox_input")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)


class DuckDuckGoResultPage:
    SEARCH_RESULTS = (By.CSS_SELECTOR, "li[data-layout='organic']")
    SEARCH_INPUT = (By.ID, 'search_form_input')
    @classmethod
    def PHRASE_RESULTS(cls, phrase):
        xpath = f"//li[@data-layout='organic']//a[contains(@href, '{phrase}')]"
        return (By.XPATH, xpath)

    def __init__(self, browser):
        self.browser = browser

    def search_results_count(self):
        search_results = self.browser.find_elements(*self.SEARCH_RESULTS)
        return len(search_results)

    def phrase_result_count(self, phrase):
        phrase_results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
        return len(phrase_results)

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')

@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_basic_duckduckgo_search(browser):
    # Настройте данные для тест-кейса
    PHRASE = 'Dog'

    # Поиск фразы
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    # Проверка, что результаты появились
    result_page = DuckDuckGoResultPage(browser)
    assert result_page.search_results_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE

