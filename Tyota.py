# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
# from AOS_Homepage import Homepage
# from AOS_CategoryPage import CategoryPage
# from AOS_ProductPage import ProductPage
# from decimal import Decimal
# from selenium.webdriver.common.action_chains import ActionChains
#
# service_chrome = Service(r"C:\Users\Matan\QA\Drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_chrome)
# driver.get("http://www.advantageonlineshopping.com/#/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# wait = WebDriverWait(webdriver, 5)
#
# # sleep(3)
# # product_list = driver.find_elements(By.CLASS_NAME, "productName")
# # print(len(product_list))
# # product_list[0].click()
# # price1 = driver.find_element(By.CSS_SELECTOR, "div[id='Description']>h2.roboto-thin").text
# # print(price1)
# # sleep(1)
# # driver.find_element(By.CLASS_NAME, "plus").click()
# # driver.find_element(By.NAME, "save_to_cart").click()
# # driver.back()
# # sleep(3)
# # product_list = driver.find_elements(By.CLASS_NAME, "productName")
# # print(product_list[1].text)
# # product_list[1].click()
# # price2 = driver.find_element(By.CSS_SELECTOR, "div[id='Description']>h2.roboto-thin").text
# # print(price2)
# # sleep(1)
# # driver.find_element(By.CLASS_NAME, "plus").click()
# # driver.find_element(By.CLASS_NAME, "plus").click()
# # driver.find_element(By.NAME, "save_to_cart").click()
# #
# # # driver.find_element(By.ID, "20").click()
# home = Homepage(driver)
# category = CategoryPage(driver)
# product = ProductPage(driver)
# home.click_category('speakers')
# category.click_product('20')
# price = product.get_price_of_one_unit()
# product.add_one()
# product.click_add_to_cart()
# driver.back()
# sleep(2)
# category.click_product('25')
# product.click_add_to_cart()
# driver.back()
# sleep(2)
# category.click_product('24')
# product.click_add_to_cart()
# print(product.get_qty(2))
# print(type(product.get_qty(2)))
# print(price)
# print(product.get_price_per_qty(2))
# # price = Decimal(product.get_price())
# # # print(type(price))
# # # print(price*2)
# # product.hover_cart_button()
# # print(product.get_total_price())
# # print(type(product.get_total_price()))
# driver.close()
