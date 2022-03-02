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


class CreateAccountPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_username_field(self):
        return self.driver.find_element(By.NAME, "usernameRegisterPage")

    # def click_username_field(self):
    #     self.get_username_field().click()

    def type_username_field(self, username):
        self.get_username_field().send_keys(username)

    def get_email_field(self):
        return self.driver.find_element(By.NAME, "emailRegisterPage")

    def type_email_field(self, email):
        self.get_email_field().send_keys(email)

    def get_password_field(self):
        return self.driver.find_element(By.NAME, "passwordRegisterPage")

    def type_password_field(self, password):
        self.get_password_field().send_keys(password)

    def get_confirm_password_field(self):
        return self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")

    def type_confirm_password_field(self, password):
        self.get_confirm_password_field().send_keys(password)

    def get_i_agree_checkbox(self):
        return self.driver.find_element(By.NAME, "i_agree")

    def click_i_agree_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(self.get_i_agree_checkbox()))
        self.get_i_agree_checkbox().click()

    def get_register_button(self):
        return self.driver.find_element(By.ID, "register_btnundefined")

    def click_register_button(self):
        self.get_register_button().click()




