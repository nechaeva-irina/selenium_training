from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ItemPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_item(self):
        self.isRequiredFieldPresent()
        old_number = self.number_items_in_cart()
        self.driver.find_element_by_css_selector('[value="Add To Cart"]').click()
        new_number = int(old_number) + 1
        try:
            self.wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span[class="quantity"]'), str(new_number)))
        except ValueError:
            print('Item has not been added to the cart!')
        self.return_to_home_page()
        return self

    def isRequiredFieldPresent(self):
        # checking if there is required field with size
        try:
            self.driver.find_element_by_css_selector('select[name="options[Size]"]')
            size = self.driver.find_element_by_css_selector('select[name="options[Size]"]')
            self.driver.execute_script("arguments[0].selectedIndex=2", size)
        except Exception:
            pass

    def return_to_home_page(self):
        self.driver.find_element_by_css_selector('i[class="fa fa-home"]').click()
        return self

    def checkout(self):
        self.driver.find_element_by_partial_link_text('Checkout').click()
        return self

    def number_items_in_cart(self):
        number = self.driver.find_element_by_css_selector('span[class="quantity"]').text
        return number
