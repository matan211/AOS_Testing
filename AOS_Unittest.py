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
from AOS_OrderPaymentPage import OrderPaymentPage
from AOS_CreateAccountPage import CreateAccountPage
from AOS_MyOrdersPage import MyOrdersPage




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
        self.orderpaymentpage = OrderPaymentPage(self.driver)
        self.createaccountpage = CreateAccountPage(self.driver)
        self.myorderspage = MyOrdersPage(self.driver)

    def test_exercise1(self):
        expected_total_price = 0
        self.homepage.click_category('speakers')
        self.categorypage.click_product('25')
        self.productpage.add_one()
        for i in range(2):
            expected_total_price += self.productpage.get_price_of_one_unit()
        self.productpage.click_add_to_cart()
        self.driver.back()
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
        quantity2 = 1
        price2 = self.productpage.get_price_of_one_unit()
        product_name2 = self.productpage.get_name_product_page()
        """click twice the plus button in quantity field"""
        for i in range(2):
            self.productpage.add_one()
            quantity2 += 1
        self.productpage.click_add_to_cart()
        self.driver.back()

        """product index 1"""
        self.categorypage.click_product('28')
        quantity1 = 1
        product_name1 = self.productpage.get_name_product_page()
        price1 = self.productpage.get_price_of_one_unit()
        """click once the plus button in quantity field"""
        self.productpage.add_one()
        quantity1 += 1
        self.productpage.click_add_to_cart()
        self.driver.back()

        """product index 0"""
        self.categorypage.click_product('27')
        quantity0 = 1
        product_name0 = self.productpage.get_name_product_page()
        price0 = self.productpage.get_price_of_one_unit()
        self.productpage.click_add_to_cart()

        """checking total order price"""
        self.cartpage.click_cart_button()
        total_order_price = self.cartpage.get_total_order_price()
        expected_total_price = price2 * quantity2 + price1 * quantity1 + price0 * quantity0
        self.assertEqual(total_order_price, expected_total_price)

        print(f"Product name: {product_name2}, Quantity: {quantity2}, Price: {price2}")
        print(f"Product name: {product_name1}, Quantity: {quantity1}, Price: {price1}")
        print(f"Product name: {product_name0}, Quantity: {quantity0}, Price: {price0}")

    def test_exercise6(self):
        self.homepage.click_category('mice')
        """product index 1"""
        self.categorypage.click_product('29')
        quantity1 = 1
        """click twice the plus button in quantity field"""
        for i in range(2):
            self.productpage.add_one()
            quantity1 += 1
        self.productpage.click_add_to_cart()
        self.driver.back()

        """product index 0"""
        self.categorypage.click_product('28')
        quantity0 = 1
        """click once the plus button in quantity field"""
        self.productpage.add_one()
        quantity0 += 1
        self.productpage.click_add_to_cart()

        """enter cart page"""
        self.cartpage.click_cart_button()
        """click edit button"""
        self.cartpage.click_edit_button(0)
        self.productpage.add_one()
        self.productpage.click_add_to_cart()
        """enter cart page"""
        self.cartpage.click_cart_button()
        """click edit button"""
        self.cartpage.click_edit_button(1)
        self.productpage.add_one()
        self.productpage.click_add_to_cart()

        """enter cart page"""
        self.cartpage.click_cart_button()
        new_quantity0 = self.cartpage.get_product_quantity(0)
        new_quantity1 = self.cartpage.get_product_quantity(1)
        """checking section"""
        self.assertEqual(quantity0 + 1, new_quantity0)
        print(f"product 0: Old qty: {quantity0}, New qty: {new_quantity0}")
        self.assertEqual(quantity1 + 1, new_quantity1)
        print(f"product 1: Old qty: {quantity1}, New qty: {new_quantity1}")

    def test_exercise7(self):
        self.homepage.click_category('tablets')
        self.categorypage.click_product('16')
        """"""
        self.driver.back()
        page_title = self.categorypage.get_page_title()
        """Path of the Tablets category page"""
        self.assertEqual(page_title, "TABLETS")
        self.driver.back()
        contact_us_heading = self.homepage.get_contact_us()
        """Contact Us is unique to the home page"""
        self.assertEqual(contact_us_heading, "CONTACT US")

    def test_exercise8(self):
        """choose product"""
        self.homepage.click_category('tablets')
        self.categorypage.click_product('16')
        self.productpage.click_add_to_cart()
        """enter cart page"""
        self.cartpage.click_cart_button()
        """checkout"""
        self.cartpage.click_checkout_button()
        """click registration button"""
        self.orderpaymentpage.click_registration_button()
        """registration - create new account"""
        self.createaccountpage.type_username_field('israel12')
        self.createaccountpage.type_email_field('israel12@gmail.com')
        self.createaccountpage.type_password_field('Israel12')
        self.createaccountpage.type_confirm_password_field('Israel12')
        self.createaccountpage.click_i_agree_checkbox()
        self.createaccountpage.click_register_button()

        """order payment with safepay"""
        self.orderpaymentpage.click_next_button()
        self.orderpaymentpage.type_safePay_username_field('israel12')
        self.orderpaymentpage.type_safePay_password_field('Israel12')
        sleep(3)
        self.orderpaymentpage.click_pay_now_button()
        """checking section"""
        text_of_recieved_order = self.orderpaymentpage.get_receipt_for_purchase()
        """order payment success"""
        self.assertEqual(text_of_recieved_order, "ORDER PAYMENT")
        """get the order ID from order payment page"""
        orderID = self.orderpaymentpage.get_order_id()
        print(orderID)
        """checking empty cart after success purchase"""
        self.cartpage.click_cart_button()
        text_of_continue_shopping_button = self.cartpage.get_continue_shopping_button()
        # self.assertEqual(text_of_continue_shopping_button, "Your shopping cart is empty")
        """checking the order exists in user's My Orders"""
        self.homepage.click_user_icon_button()
        sleep(10)
        self.homepage.click_my_orders_button()
        sleep(5)
        last_order_ID = self.myorderspage.get_last_order_number()
        print(last_order_ID)
        self.assertEqual(last_order_ID, orderID)

        sleep(20)



    # def tearDown(self):
    #     self.driver.close()


if __name__ == '__main__':
    unittest.main()
