import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


@pytest.fixture
def driver(request):
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'browser': 'ALL'}
    wd = webdriver.Chrome(desired_capabilities=caps)
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def login(driver):
    driver.get('http://localhost/litecart/admin/')
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()


def test_logs_17(driver):
    login(driver)
    driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')
    driver.find_element_by_link_text('Subcategory').click()
    rows = driver.find_elements_by_css_selector('tr[class="row"]')[3:]
    list = []
    for row in rows:
        link_in_row = row.find_element_by_css_selector('td a')
        list.append(link_in_row.get_attribute('href'))

    logs_list = []
    for i in list:
        driver.get(i)

        for l in driver.get_log("browser"):
            print(l)
            logs_list.append(l)

    assert len(logs_list) == 0
