from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def remove_all_items(self):
        self.stop_changing_items()
        number_of_products_in_cart = self.driver.find_elements_by_css_selector('tr td[class="item"]')
        for i in range(0, len(number_of_products_in_cart)):
            table = self.driver.find_element_by_id('box-checkout-summary')
            self.driver.find_element_by_css_selector('[name="remove_cart_item"]').click()
            WebDriverWait(self.driver, 3).until(EC.staleness_of(table))
        return self

    def stop_changing_items(self):
        # stop changing items in preview if number of items > 1
        try:
            self.driver.find_element_by_css_selector('li[class="shortcut"]').click()
        except Exception:
            pass

    def final_message(self):
        message = self.driver.find_element_by_css_selector('p em').text
        return message
