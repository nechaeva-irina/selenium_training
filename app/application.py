from selenium import webdriver
from pages.main_page import MainPage
from pages.item_page import ItemPage
from pages.cart_page import CartPage


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.main_page = MainPage(self.driver)
        self.item_page = ItemPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def quit(self):
        self.driver.quit()
