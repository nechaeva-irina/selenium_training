import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string
import random


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def random_generator(size):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(size)])


email = random_generator(6) + '@localhost.ru'
password = random_generator(8)


def test_create_account_11(driver):
    driver.get("http://localhost/litecart/")
    driver.find_element_by_xpath('//*[@id="box-account-login"]/div/form/table/tbody/tr[5]/td/a').click()
    user_creation(driver, 'Ivanov', 'Ivan', '5th avenue str.64', '12345', 'New Your', '+375731112233')
    logout(driver)
    login(driver)
    logout(driver)


def login(driver):
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_css_selector('button[value="Login"]').click()


def logout(driver):
    driver.find_element_by_link_text('Logout').click()


def user_creation(driver, firstname, lastname, address1, postcode, city, phone):
    driver.find_element_by_name('firstname').send_keys(firstname)
    driver.find_element_by_name('lastname').send_keys(lastname)
    driver.find_element_by_name('address1').send_keys(address1)
    driver.find_element_by_name('postcode').send_keys(postcode)
    driver.find_element_by_name('city').send_keys(city)
    driver.find_element_by_css_selector('.select2-selection__arrow').click()
    driver.find_element_by_css_selector('input[type="search"]').send_keys('United States', Keys.ENTER)
    driver.find_element_by_css_selector('select[name="zone_code"]').click()
    driver.find_element_by_css_selector('select option[value="CT"]').click()
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('phone').send_keys(phone)
    value_checkbox = driver.find_element_by_name('newsletter').get_attribute('checked')
    print(value_checkbox)
    if value_checkbox:
        driver.find_element_by_name('newsletter').click()
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('confirmed_password').send_keys(password)
    driver.find_element_by_name('create_account').click()
