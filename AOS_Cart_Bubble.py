from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from decimal import Decimal
from AOS_ProductPage import ProductPage

class CartBubble:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.productpage = ProductPage(self.driver)

    def get_remove_button(self, index):
        self.productpage.hover_cart_button()
        remove_buttons_list = self.driver.find_elements(By.CLASS_NAME, "removeProduct")
        return remove_buttons_list[index]

    def click_remove_button(self, index):
        self.get_remove_button(index).click()

    def get_total_items(self):
        self.productpage.hover_cart_button()
        return self.driver.find_element(By.CSS_SELECTOR, "label.roboto-regular").text

