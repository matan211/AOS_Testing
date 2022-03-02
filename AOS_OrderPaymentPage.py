from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
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
        self.wait.until(EC.presence_of_element_located((By.ID, "next_btn")))
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
        self.wait.until(EC.presence_of_element_located((By.ID, "pay_now_btn_SAFEPAY")))
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

    """login to existing account after checkout"""
    def get_username_field(self):
        return self.driver.find_element(By.NAME, "usernameInOrderPayment")

    def type_username_field(self, username):
        self.get_username_field().send_keys(username)

    def get_password_field(self):
        return self.driver.find_element(By.NAME, "passwordInOrderPayment")

    def type_password_field(self, password):
        self.get_password_field().send_keys(password)

    def get_login_button(self):
        self.driver.find_element(By.ID, "login_btnundefined").click()

    # def click_login_button(self):
    #     self.get_login_button().click()

    """pay with master credit card"""
    def get_master_credit_button(self):
        self.wait.until(EC.presence_of_element_located((By.NAME, "masterCredit")))
        self.driver.find_element(By.NAME, "masterCredit").click()
    #
    # def click_master_credit_button(self):
    #     self.get_master_credit_button().click()

    def get_edit_button(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "edit")))
        return self.driver.find_element(By.CLASS_NAME, "edit")

    def click_edit_button(self):
        self.get_edit_button().click()

    """type card number"""
    def get_card_number_field(self):
        return self.driver.find_element(By.ID, "creditCard")

    def type_card_number_field(self, card_number):
        self.clear_card_number_field()
        self.get_card_number_field().send_keys(card_number)

    def clear_card_number_field(self):
        self.get_card_number_field().clear()

    """type cvv number"""

    def get_cvv_field(self):
        return self.driver.find_element(By.NAME, "cvv_number")

    def type_cvv_field(self, cvv):
        self.click_cvv_field()
        self.get_cvv_field().send_keys(cvv)

    def clear_cvv_field(self):
        self.get_cvv_field().clear()

    def click_cvv_field(self):
        self.get_cvv_field().click()

    """type card holder name"""

    def get_card_holder_field(self):
        return self.driver.find_element(By.NAME, "cardholder_name")

    def type_card_holder_field(self, name):
        self.clear_card_holder_field()
        self.get_card_holder_field().send_keys(name)

    def clear_card_holder_field(self):
        self.get_card_holder_field().clear()

    """select month"""

    def get_month_dropdown(self):
        return self.driver.find_element(By.NAME, "mmListbox")

    def click_month_dropdown(self):
        self.get_month_dropdown().click()

    def select_month_dropdown(self, month):
        self.wait.until(EC.presence_of_element_located((By.NAME, "mmListbox")))
        sel = Select(self.get_month_dropdown())
        sel.select_by_visible_text(month)

    """select year"""

    def get_year_dropdown(self):
        return self.driver.find_element(By.NAME, "yyyyListbox")

    def click_year_dropdown(self):
        self.get_year_dropdown().click()

    def select_year_dropdown(self, year):
        self.wait.until(EC.presence_of_element_located((By.NAME, "yyyyListbox")))
        sel = Select(self.get_year_dropdown())
        sel.select_by_visible_text(year)

    def get_pay_now_master_credit(self):
        return self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")

    def click_pay_now_master_credit(self):
        self.get_pay_now_master_credit().click()









