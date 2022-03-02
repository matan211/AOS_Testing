from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from decimal import Decimal
from AOS_ProductPage import ProductPage

class LoginPopUp:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_login_username_field(self):
        return self.driver.find_element(By.NAME, 'username')

    def type_login_username_field(self, username):
        self.get_login_username_field().send_keys(username)

    def get_login_password_field(self):
        return self.driver.find_element(By.NAME, "password")

    def type_login_password_field(self, password):
        self.get_login_password_field().send_keys(password)

    def get_sign_in_button(self):
        return self.driver.find_element(By.ID, 'sign_in_btnundefined')

    def click_sign_in_button(self):
        self.get_sign_in_button().click()
