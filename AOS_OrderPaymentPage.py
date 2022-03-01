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

class OrderPaymentPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_registration_button(self):
        return self.driver.find_element(By.ID, "registration_btnundefined")

    def click_registration_button(self):
        self.get_registration_button().click()

    def get_next_button(self):
        return self.driver.find_element(By.ID, "next_btn")

    def click_next_button(self):
        self.get_next_button().click()

    def get_safePay_username_field(self):
        return self.driver.find_element(By.NAME, "safepay_username")

    def type_safePay_username_field(self, username):
        self.get_safePay_username_field().send_keys(username)

    def get_safePay_password_field(self):
        return self.driver.find_element(By.NAME, "safepay_password")

    def type_safePay_password_field(self, password):
        self.get_safePay_password_field().send_keys(password)

    def get_pay_now_button(self):
        return self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")

    def click_pay_now_button(self):
        self.get_pay_now_button().click()

    def get_receipt_for_purchase(self):
        return self.driver.find_element(By.CSS_SELECTOR, "article>h3.roboto-regular").text

    def get_order_id(self):
        order_id_element_text = ''
        while order_id_element_text == '':
            try:
                order_id_element = self.driver.find_element(By.CSS_SELECTOR, "label#orderNumberLabel")
                order_id_element_text = order_id_element.text
            except:
                pass
        return order_id_element_text
