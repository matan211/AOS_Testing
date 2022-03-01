from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CategoryPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_product(self, product_id):
        return self.driver.find_element(By.ID, product_id)

    def click_product(self, product_id):
        self.get_product(product_id).click()

    def get_page_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='select  ng-binding']").text

