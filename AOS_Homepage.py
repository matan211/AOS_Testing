from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from AOS_LoginPopUp import LoginPopUp

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

    def get_user_icon_button(self):
        return self.driver.find_element(By.ID, 'menuUser')

    def click_user_icon_button(self):
        self.get_user_icon_button().click()

    def get_my_orders_button(self):
        while True:
            try:
                elements_list = self.driver.find_elements(By.CSS_SELECTOR, "label.option[translate='My_Orders']")
                return elements_list[1]
            except:
                pass

    def click_my_orders_button(self):
        while True:
            try:
                self.get_my_orders_button().click()
                break
            except:
                pass

    def get_sign_out_button(self):
        """the list has 2 elements. The second one is the sign out button"""
        elements_list = self.driver.find_elements(By.CSS_SELECTOR, "[translate='Sign_out']")
        return elements_list[1]

    def click_sign_out_button(self):
        self.get_sign_out_button().click()

    def get_verify_for_user(self):
        self.wait.until(EC.presence_of_element_located((By.ID, 'menuUser')))
        sleep(1)
        return self.driver.find_element(By.CSS_SELECTOR, ".hi-user.containMiniTitle").text



