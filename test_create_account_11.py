import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_create_account_11(driver):
    driver.get("http://localhost/litecart/")
    driver.find_element_by_xpath('//*[@id="box-account-login"]/div/form/table/tbody/tr[5]/td/a').click()
    driver.find_element_by_name('firstname').send_keys('Aleksandr')
    driver.find_element_by_name('lastname').send_keys('Aleksandrov')
    driver.find_element_by_name('address1').send_keys('5th Avenue str. 26')
    driver.find_element_by_name('postcode').send_keys('12345')
    driver.find_element_by_name('city').send_keys('New York')
    driver.find_element_by_css_selector('.select2-selection__arrow').click()
    driver.find_element_by_css_selector('input[type="search"]').send_keys('United States', Keys.ENTER)
    driver.find_element_by_css_selector('select[name="zone_code"]').click()
    driver.find_element_by_css_selector('select option[value="CT"]').click()
    driver.find_element_by_name('email').send_keys('qwerty@localhost')
    driver.find_element_by_name('phone').send_keys('+176846-10-33')
    value_checkbox = driver.find_element_by_name('newsletter').get_attribute('checked')
    print(value_checkbox)
    if value_checkbox:
        driver.find_element_by_name('newsletter').click()
    driver.find_element_by_name('password').send_keys('secret')
    driver.find_element_by_name('confirmed_password').send_keys('secret')
    driver.find_element_by_name('create_account').click()
    driver.find_element_by_link_text('Logout').click()
    driver.find_element_by_name('email').send_keys('qwerty@localhost')
    driver.find_element_by_name('password').send_keys('secret')
    driver.find_element_by_css_selector('button[value="Login"]').click()
    driver.find_element_by_link_text('Logout').click()





