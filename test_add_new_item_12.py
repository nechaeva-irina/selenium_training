import pytest
from selenium import webdriver
import os


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_add_new_item_12(driver):
    login(driver)
    driver.find_element_by_link_text('Catalog').click()
    driver.find_element_by_link_text('Add New Product').click()
    # Fill-in General tab
    driver.find_elements_by_css_selector('input[name="status"]')[0].click()
    driver.find_element_by_name('name[en]').send_keys('Funny duck')
    driver.find_element_by_name('code').send_keys('F212LT')
    driver.find_element_by_css_selector('input[data-name="Subcategory"]').click()
    driver.find_element_by_css_selector('input[value="1-3"]').click()
    driver.find_element_by_css_selector('input[name="quantity"]').clear()
    driver.find_element_by_css_selector('input[name="quantity"]').send_keys('77')
    sold_out_status = driver.find_element_by_name('sold_out_status_id')
    driver.execute_script("arguments[0].selectedIndex=2", sold_out_status)
    dirname = os.path.dirname(__file__)
    filename = '123.jpeg'
    path = os.path.join(dirname, filename)
    driver.find_element_by_css_selector('input[type="file"]').send_keys(path)
    driver.find_element_by_css_selector('input[name="date_valid_from"]').send_keys('2021-01-11')
    driver.find_element_by_css_selector('input[name="date_valid_to"]').send_keys('2021-12-20')
    # Fill-in Information tab
    driver.find_element_by_link_text('Information').click()
    Manufacturer = driver.find_element_by_name('manufacturer_id')
    driver.execute_script("arguments[0].selectedIndex=1", Manufacturer)
    driver.find_element_by_name('keywords').send_keys('yellow_dark')
    driver.find_element_by_name('short_description[en]').send_keys('This is short description')
    driver.find_element_by_css_selector('div[class="trumbowyg-editor"]').send_keys(
        'Something that describe the product')
    driver.find_element_by_name('head_title[en]').send_keys('Funny yellow duck')
    # Fill-in Prices tab
    driver.find_element_by_link_text('Prices').click()
    driver.find_element_by_name('purchase_price').clear()
    driver.find_element_by_name('purchase_price').send_keys('12')
    currency = driver.find_element_by_name('purchase_price_currency_code')
    driver.execute_script("arguments[0].selectedIndex=2", currency)
    driver.find_element_by_name('prices[USD]').send_keys('18')
    driver.find_element_by_name('prices[EUR]').send_keys('16')
    driver.find_element_by_css_selector('button[name="save"]').click()


def login(driver):
    driver.get('http://localhost/litecart/admin/')
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
