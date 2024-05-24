from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService


browser = webdriver.Chrome()
URL = "https://qa-test-selectors.netlify.app/"

try:
    browser.get(URL)
    browser.implicitly_wait(10)

    elements_by_tag = browser.find_elements(By.TAG_NAME, "h1")
    print("Элементы с тегом h1:", len(elements_by_tag))

    elements_by_name = browser.find_elements(By.NAME, "blackWhite-rabbit")
    print("Элементы с именем blackWhite-rabbit:", len(elements_by_name))

    elements_by_class = browser.find_elements(By.CLASS_NAME, "imageContainer")
    print("Элементы с классом imageContainer:", len(elements_by_class))

    elements_by_id = browser.find_elements(By.ID, "blackWhite")
    print("Элементы с ID blackWhite:", len(elements_by_id))

    elements_by_selector = browser.find_elements(By.CSS_SELECTOR,'[data-type="image"]')
    print("Элементы с data-type image:", len(elements_by_selector))
finally:
    browser.quit()