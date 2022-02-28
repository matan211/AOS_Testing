import unittest
from AOS_Homepage import Homepage
from AOS_CategoryPage import CategoryPage
from AOS_ProductPage import ProductPage
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep


class MyTestCase(unittest.TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\Users\Matan\QA\Drivers.chromedriver.exe")

        self.driver = webdriver.Chrome(service=service_chrome)

        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        sleep(1)
        self.homepage = Homepage(self.driver)
        self.categorypage = CategoryPage(self.driver)
        self.productpage = ProductPage(self.driver)

    def exercise1(self):
        expected_total_price = 0
        self.homepage.click_category('speakers')
        self.categorypage.click_product('25')
        self.productpage.add_one()
        expected_total_price += self.productpage.get_price()
        self.productpage.click_add_to_cart()
        self.driver.back()
        # sleep(1)
        self.categorypage.click_product('20')
        for i in range(2):
            self.productpage.add_one()
            expected_total_price += self.productpage.get_price()
        self.productpage.click_add_to_cart()
        total_price = self.productpage.get_total_price()
        self.assertEqual(expected_total_price, total_price)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
