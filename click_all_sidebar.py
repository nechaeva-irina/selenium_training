import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    for i in range(0, len(driver.find_elements_by_css_selector(".name"))):
        driver.find_elements_by_css_selector(".name")[i].click()
        are_elements_present(driver, By.CSS_SELECTOR, "h1")
        if len(driver.find_elements_by_css_selector("ul.docs")) > 0:
            for i2 in range(0, len(driver.find_elements_by_css_selector("ul.docs > li"))):
                driver.find_elements_by_css_selector("ul.docs > li")[i2].click()
                are_elements_present(driver, By.CSS_SELECTOR, "h1")
            driver.find_element_by_css_selector('[title="My Store"]').click()
        else:
            continue
        driver.find_element_by_css_selector('[title="My Store"]').click()


def are_elements_present(driver, x, y):
    return len(driver.find_elements(x, y)) > 0
