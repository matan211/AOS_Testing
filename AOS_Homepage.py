from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homepage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_category(self, category):
        id = category + 'Img'
        return self.driver.find_element(By.ID, id)

    def click_category(self, category):
        self.get_category(category).click()

    """Contact Us heading is unique to the home page"""
    def get_contact_us(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h1.roboto-bold").text
