import unittest
from AOS_Homepage import Homepage
from AOS_CategoryPage import CategoryPage
from AOS_ProductPage import ProductPage
from AOS_Cart_Bubble import CartBubble
from AOS_CartPage import CartPage
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
from decimal import Decimal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class MyTestCase(unittest.TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\Users\Matan\QA\Drivers\chromedriver.exe")

        self.driver = webdriver.Chrome(service=service_chrome)

        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        sleep(1)
        self.homepage = Homepage(self.driver)
        self.categorypage = CategoryPage(self.driver)
        self.productpage = ProductPage(self.driver)
        self.cartbubble = CartBubble(self.driver)
        self.cartpage = CartPage(self.driver)

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

        """goes back to home page"""
        self.driver.back()
        self.driver.back()



    """checks that the products in the cart bubble are same to the chosen products"""
    """checks name, color, quantity, price"""

    def test_exercise2(self):
        self.homepage.click_category('speakers')
        """product index 2"""
        self.categorypage.click_product('21')
        price2 = self.productpage.get_price_of_one_unit()
        """click twice the plus button in quantity field"""
        for i in range(2):
            self.productpage.add_one()
        self.productpage.click_add_to_cart()
        self.driver.back()

        """product index 1"""
        self.categorypage.click_product('25')
        price1 = self.productpage.get_price_of_one_unit()
        """click once the plus button in quantity field"""
        self.productpage.add_one()
        self.productpage.click_add_to_cart()
        self.driver.back()

        """product index 0"""
        self.categorypage.click_product('24')
        price0 = self.productpage.get_price_of_one_unit()
        self.productpage.click_add_to_cart()

        """testing section"""

        self.assertEqual(self.productpage.get_product_name(0), 'HP ROAR MINI WIRELESS SPEAKER')
        self.assertEqual(self.productpage.get_color_name(0), 'RED')
        self.assertEqual(self.productpage.get_qty(0), Decimal('1'))
        self.assertEqual(self.productpage.get_price_per_qty(0), self.productpage.get_qty(0) * price0)

        self.assertEqual(self.productpage.get_product_name(1), 'BOSE SOUNDLINK WIRELESS SPE...')
        self.assertEqual(self.productpage.get_color_name(1), 'TURQUOISE')
        self.assertEqual(self.productpage.get_qty(1), Decimal('2'))
        self.assertEqual(self.productpage.get_price_per_qty(1), self.productpage.get_qty(1) * price1)

        self.assertEqual(self.productpage.get_product_name(2), 'HP ROAR PLUS WIRELESS SPEAKER')
        self.assertEqual(self.productpage.get_color_name(2), 'BLUE')
        self.assertEqual(self.productpage.get_qty(2), Decimal('3'))
        self.assertEqual(self.productpage.get_price_per_qty(2), self.productpage.get_qty(2) * price2)

        """goes back to home page"""
        self.driver.back()
        self.driver.back()


    """checks that the removes product is gone from the cart bubble"""
    def test_exercise3(self):
        self.homepage.click_category('speakers')
        """product index 1"""
        self.categorypage.click_product('21')
        self.productpage.click_add_to_cart()
        self.driver.back()

        """product index 0"""
        self.categorypage.click_product('20')
        self.productpage.click_add_to_cart()

        self.cartbubble.click_remove_button(1)

        """testing section"""
        total_items = self.cartbubble.get_total_items()
        self.assertEqual(total_items, "(1 Item)")

        self.driver.back()
        self.driver.back()

    def test_exercise4(self):
        """buy product"""
        self.homepage.click_category('speakers')
        self.categorypage.click_product('21')
        self.productpage.click_add_to_cart()

        self.cartpage.click_cart_button()
        logo_text = self.cartpage.get_shopping_cart_logo_name()
        self.assertEqual(logo_text, "SHOPPING CART")

        self.driver.back()
        self.driver.back()

    def test_exercise5(self):
        self.homepage.click_category('mice')
        """product index 2"""
        self.categorypage.click_product('29')
        price2 = self.productpage.get_price_of_one_unit()
        """click twice the plus button in quantity field"""
        for i in range(2):
            self.productpage.add_one()
        self.productpage.click_add_to_cart()
        self.driver.back()

        """product index 1"""
        self.categorypage.click_product('28')
        price1 = self.productpage.get_price_of_one_unit()
        """click once the plus button in quantity field"""
        self.productpage.add_one()
        self.productpage.click_add_to_cart()
        self.driver.back()

        """product index 0"""
        self.categorypage.click_product('27')
        price0 = self.productpage.get_price_of_one_unit()
        self.productpage.click_add_to_cart()

        self.cartpage.click_cart_button()
        total_order_price = self.cartpage.get_total_order_price()
        expected_total_price = price2 * 3 + price1 * 2 + price0
        self.assertEqual(total_order_price, expected_total_price)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
