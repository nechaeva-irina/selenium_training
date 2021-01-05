import pytest
from selenium import webdriver
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_zones_are_sorted_9_2(driver):
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    rows = driver.find_elements_by_css_selector('tr.row')
    for i in range(0, len(rows)):
        cell_with_name = driver.find_elements_by_css_selector('tr.row a:not([title])')[i]
        link = cell_with_name.get_attribute('href')
        driver.get(link)
        rows_inside = driver.find_elements_by_css_selector('table#table-zones tr')[1:-1]
        list_of_zones = []
        for el in range(0, len(rows_inside)):
            one_row = rows_inside[el]
            cell_with_zone = one_row.find_elements_by_css_selector('td')[2]
            selected_zone = cell_with_zone.find_element_by_css_selector('[selected = selected]')
            zone_name = selected_zone.get_attribute('textContent')
            list_of_zones.append(zone_name)
            print('%s. ' % (el + 1) + zone_name)
        if list_of_zones == sorted(list_of_zones):
            print('\nWell done! Zones  are in alphabetic order\n')
        else:
            print('\nOops, something went wrong. Zones are NOT in alphabetic order\n')
        driver.find_element_by_css_selector('button[name="cancel"]').click()
