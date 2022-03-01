from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from decimal import Decimal
from time import sleep


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

    def get_price_of_one_unit(self):
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
        total_price = elements_list[1].text[1:]
        if total_price[1] == ',':
            total_price = total_price[0]+total_price[2:]
        return Decimal(total_price)

    def get_product_name(self,index):
        self.hover_cart_button()
        products_list = self.driver.find_elements(By.CSS_SELECTOR, "a>h3.ng-binding")
        return products_list[index].text

    def get_color_name(self, index):
        self.hover_cart_button()
        products_list = self.driver.find_elements(By.CSS_SELECTOR, "label.ng-binding>span.ng-binding")
        return products_list[index].text

    """get quantity of product in cart bubble"""
    def get_qty(self, index):
        self.hover_cart_button()
        while True:
            try:
                products_list = self.driver.find_elements(By.CSS_SELECTOR, "a>label.ng-binding")
                qty_products_list = products_list[::2]
                return Decimal(qty_products_list[index].text[5:])
            except:
                pass

    def get_price_per_qty(self, index):
        self.hover_cart_button()
        while True:
            try:

                products_list = self.driver.find_elements(By.CSS_SELECTOR, "[class='price roboto-regular ng-binding']")
                return Decimal(products_list[index].text[1:])
            except:
                pass

    def get_name_product_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='roboto-regular screen768 ng-binding']").text


