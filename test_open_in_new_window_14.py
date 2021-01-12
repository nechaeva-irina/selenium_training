import pytest
from selenium import webdriver
from random import randrange
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def login(driver):
    driver.get('http://localhost/litecart/admin/')
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()


def test_add_new_item_12(driver):
    login(driver)
    driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
    list_of_countries = driver.find_elements_by_css_selector('i[class="fa fa-pencil"]')
    index_to_edit = randrange(len(list_of_countries))
    list_of_countries[index_to_edit].click()

    external_links = driver.find_elements_by_css_selector('i[class="fa fa-external-link"]')
    for el in external_links:
        main_window = driver.current_window_handle
        el.click()
        WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
        new_windows = driver.window_handles
        new_window = new_windows[1]
        driver.switch_to.window(new_window)
        driver.close()
        driver.switch_to.window(main_window)
