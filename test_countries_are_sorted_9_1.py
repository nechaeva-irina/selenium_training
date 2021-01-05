import pytest
from selenium import webdriver
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_countries_are_sorted(driver):
    login(driver)
    number_of_rows = len(driver.find_elements_by_css_selector('tr.row'))
    print(number_of_rows)
    list_of_countries = []
    for i in range(0, number_of_rows):
        row = driver.find_elements_by_css_selector('tr.row')[i]
        country = row.find_elements_by_css_selector('td')[4].text
        list_of_countries.append(country)
        print('%s. ' % (i + 1) + country)
    if list_of_countries == sorted(list_of_countries):
        print('Countries are in alphabetical order')
    else:
        print('Countries are NOT in alphabetical order')


def test_zones_are_sorted(driver):
    login(driver)
    number_of_rows = len(driver.find_elements_by_css_selector('tr.row'))
    for i in range(0, number_of_rows):
        row = driver.find_elements_by_css_selector('tr.row')[i]
        if int(row.find_elements_by_css_selector('td')[5].text) > 0:
            driver.find_elements_by_css_selector('i[class="fa fa-pencil"]')[i].click()
            rows_in_zones_table = driver.find_elements_by_css_selector('table#table-zones tr')[1:-1]
            print(len(rows_in_zones_table))
            list_of_zones = []
            for el in range(0, len(rows_in_zones_table)):
                one_row = rows_in_zones_table[el]
                zone = one_row.find_elements_by_css_selector('td')[2].text
                list_of_zones.append(zone)
                print('%s. ' % (el + 1) + zone)
            if list_of_zones == sorted(list_of_zones):
                print('Well done! Zones are in alphabetic order')
            else:
                print('Oops, something went wrong. Zones are NOT in alphabetic order')
            time.sleep(2)
            driver.find_element_by_css_selector('button[name="save"]').click()


def login(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
