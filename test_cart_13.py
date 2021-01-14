import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_cart_13(driver):
    driver.get("http://localhost/litecart/")
    for i in range(0, 3):
        driver.find_elements_by_css_selector('img[class="image"]')[0].click()
        number_in_cart = int(driver.find_element_by_css_selector('span[class="quantity"]').text)
        new_number = str(number_in_cart + 1)
        # checking if there is required field with size
        if isElementPresent(driver, 'select[name="options[Size]"]'):
            time.sleep(1)
            size = driver.find_element_by_css_selector('select[name="options[Size]"]')
            driver.execute_script("arguments[0].selectedIndex=2", size)
        driver.find_element_by_css_selector('[value="Add To Cart"]').click()
        WebDriverWait(driver, 3).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span[class="quantity"]'), new_number))
        driver.find_element_by_css_selector('i[class="fa fa-home"]').click()
    driver.find_element_by_partial_link_text('Checkout').click()
    # stop changing items in preview if number of items > 1
    try:
        driver.find_element_by_css_selector('li[class="shortcut"]').click()
    except Exception:
        pass
    # delete items from the cart
    number_of_products_in_cart = driver.find_elements_by_css_selector('tr td[class="item"]')
    for i in range(0, len(number_of_products_in_cart)):
        table = driver.find_element_by_id('box-checkout-summary')
        driver.find_element_by_css_selector('[name="remove_cart_item"]').click()
        WebDriverWait(driver, 3).until(EC.staleness_of(table))


def isElementPresent(driver, locator):
    try:
        driver.find_element_by_css_selector(locator)
    except NoSuchElementException:
        return False
    return True
