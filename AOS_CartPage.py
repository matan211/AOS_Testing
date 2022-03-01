from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from decimal import Decimal
from AOS_ProductPage import ProductPage
from time import sleep

class CartPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.productpage = ProductPage(self.driver)

    def click_cart_button(self):
        self.productpage.get_cart_button().click()

    def get_shopping_cart_logo_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='select  ng-binding']").text

    def get_total_order_price_locator(self):
        while True:
            try:
                elements_list = self.driver.find_elements(By.CSS_SELECTOR, "td[colspan='2']>span[class='roboto-medium ng-binding']")
                return elements_list[1]
            except:
                pass

    def get_total_order_price(self):
        element = self.get_total_order_price_locator()
        return Decimal(element.text[1:])
