import unittest
from AOS_Homepage import Homepage
from AOS_CategoryPage import CategoryPage
from AOS_ProductPage import ProductPage
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
from decimal import Decimal


class MyTestCase(unittest.TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\Users\Matan\QA\Drivers\chromedriver.exe")

        self.driver = webdriver.Chrome(service=service_chrome)

        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        sleep(1)
        self.homepage = Homepage(self.driver)
        self.categorypage = CategoryPage(self.driver)
        self.productpage = ProductPage(self.driver)

    def test_exercise1(self):
        expected_total_price = 0
        self.homepage.click_category('speakers')
        self.categorypage.click_product('25')
        self.productpage.add_one()
        for i in range(2):
            expected_total_price += self.productpage.get_price_of_one_unit()
        self.productpage.click_add_to_cart()
        self.driver.back()
        # sleep(1)
        self.categorypage.click_product('20')
        for i in range(2):
            self.productpage.add_one()
            expected_total_price += self.productpage.get_price_of_one_unit()
        expected_total_price += self.productpage.get_price_of_one_unit()
        self.productpage.click_add_to_cart()
        total_price = self.productpage.get_total_price()
        self.assertEqual(expected_total_price, total_price)

    def test_exercise2(self):
        self.homepage.click_category('speakers')
        """index 2"""
        self.categorypage.click_product('20')
        price2 = self.productpage.get_price_of_one_unit()
        for i in range(2):
            self.productpage.add_one()
        self.productpage.click_add_to_cart()
        self.driver.back()
        """index 1"""
        self.categorypage.click_product('25')
        price1 = self.productpage.get_price_of_one_unit()
        self.productpage.add_one()
        self.productpage.click_add_to_cart()
        self.driver.back()
        """index 0"""
        self.categorypage.click_product('24')
        price0 = self.productpage.get_price_of_one_unit()
        self.productpage.click_add_to_cart()

        self.assertEqual(self.productpage.get_product_name(0), 'HP ROAR MINI WIRELESS SPEAKER')
        self.assertEqual(self.productpage.get_color_name(0), 'RED')
        self.assertEqual(self.productpage.get_qty(0), Decimal('1'))
        self.assertEqual(self.productpage.get_price_per_qty(0), self.productpage.get_qty(0) * price0)

        self.assertEqual(self.productpage.get_product_name(1), 'BOSE SOUNDLINK WIRELESS SPE...')
        self.assertEqual(self.productpage.get_color_name(1), 'TURQUOISE')
        self.assertEqual(self.productpage.get_qty(1), Decimal('2'))
        self.assertEqual(self.productpage.get_price_per_qty(1), self.productpage.get_qty(1) * price1)

        self.assertEqual(self.productpage.get_product_name(2), 'BOSE SOUNDLINK BLUETOOTH SP...')
        self.assertEqual(self.productpage.get_color_name(2), 'BLACK')
        self.assertEqual(self.productpage.get_qty(2), Decimal('3'))
        self.assertEqual(self.productpage.get_price_per_qty(2), self.productpage.get_qty(2) * price2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
