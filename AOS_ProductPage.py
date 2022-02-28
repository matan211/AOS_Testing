from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from decimal import Decimal


class ProductPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_plus(self):
        return self.driver.find_element(By.CLASS_NAME, "plus")

    def add_one(self):
        self.get_plus().click()

    def add_to_cart(self):
        return self.driver.find_element(By.NAME, "save_to_cart")

    def click_add_to_cart(self):
        self.add_to_cart().click()

    def get_price(self):
        price = self.driver.find_element(By.CSS_SELECTOR, "div[id='Description']>h2.roboto-thin").text[1:]
        return Decimal(price)

    def get_cart_button(self):
        return self.driver.find_element(By.ID, "menuCart")

    def hover_cart_button(self):
        hover = ActionChains(self.driver).move_to_element(self.get_cart_button())
        hover.perform()

    def get_total_price(self):
        self.hover_cart_button()
        elements_list = self.driver.find_elements(By.CSS_SELECTOR, "td>span.roboto-medium")
        return Decimal(elements_list[1].text[1:])


