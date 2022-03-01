from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from decimal import Decimal
from time import sleep


class MyOrdersPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_last_order_number(self):
        elements_list = self.driver.find_elements(By.CSS_SELECTOR, "tr.ng-scope[data-ng-repeat-start='order in "
                                                                   "myOrdersCtrl.orders track by $index']>td["
                                                                   "rowspan='1']>label.ng-binding")
        return elements_list[len(elements_list) - 4].text
