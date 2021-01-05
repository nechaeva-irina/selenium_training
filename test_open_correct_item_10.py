import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_open_correct_item_10(driver):
    driver.get("http://localhost/litecart/")
    """
    MP is main page
    IP is item page
    """
    name_on_MP = driver.find_element_by_css_selector('div#box-campaigns .name').text
    regular_price_MP = driver.find_element_by_css_selector('s[class="regular-price"]').text
    campaign_price_MP = driver.find_element_by_css_selector('strong[class="campaign-price"]').text
    regular_price_color_MP = driver.find_element_by_css_selector('s[class="regular-price"]').value_of_css_property(
        'color')
    campaign_price_color_MP = driver.find_element_by_css_selector(
        'strong[class="campaign-price"]').value_of_css_property('color')
    regular_price_size_MP = driver.find_element_by_css_selector('s[class="regular-price"]').value_of_css_property(
        'font-size')
    campaign_price_size_MP = driver.find_element_by_css_selector(
        'strong[class="campaign-price"]').value_of_css_property('font-size')
    driver.find_element_by_css_selector('div#box-campaigns a[class="link"]').click()
    name_on_IP = driver.find_element_by_css_selector('h1').get_attribute('textContent')
    regular_price_IP = driver.find_element_by_css_selector('s[class="regular-price"]').text
    campaign_price_IP = driver.find_element_by_css_selector('strong[class="campaign-price"]').text
    regular_price_color_IP = driver.find_element_by_css_selector('s[class="regular-price"]').value_of_css_property(
        'color')
    campaign_price_color_IP = driver.find_element_by_css_selector(
        'strong[class="campaign-price"]').value_of_css_property('color')
    regular_price_size_IP = driver.find_element_by_css_selector('s[class="regular-price"]').value_of_css_property(
        'font-size')
    campaign_price_size_IP = driver.find_element_by_css_selector(
        'strong[class="campaign-price"]').value_of_css_property('font-size')
    assert name_on_MP == name_on_IP
    assert regular_price_MP == regular_price_IP
    assert campaign_price_MP == campaign_price_IP
    """
    Because of different interpretation of color in Chrome (rgba(102, 102, 102, 1)) and Firefox(rgb(102, 102, 102)), 
    firstly split str by '(' and leave part with index [1] to have the same indexes of values R,G and B for compare.
    """
    assert (regular_price_color_MP.split('(')[1])[0:3] == (regular_price_color_MP.split('(')[1])[5:8] == (
                                                                                                         regular_price_color_MP.split(
                                                                                                             '(')[1])[
                                                                                                         10:13]
    assert (regular_price_color_IP.split('(')[1])[0:3] == (regular_price_color_IP.split('(')[1])[5:8] == (
                                                                                                             regular_price_color_IP.split(
                                                                                                                 '(')[
                                                                                                                 1])[
                                                                                                         10:13]
    assert campaign_price_color_MP.count(' 0') >= 2
    assert campaign_price_color_IP.count(' 0') >= 2
    assert float(regular_price_size_MP[0:-2]) < float(campaign_price_size_MP[0:-2])
    assert int(regular_price_size_IP[0:-2]) < int(campaign_price_size_IP[0:-2])


"""
These asserts work only in Chrome browser:
assert regular_price_color_IP[5:8] == regular_price_color_IP[10:13] == regular_price_color_IP[15:18]
assert regular_price_color_IP[5:8] == regular_price_color_IP[10:13] == regular_price_color_IP[15:18]
assert int(campaign_price_color_MP[10]) == 0 and  int(campaign_price_color_MP[13]) == 0
assert int(campaign_price_color_IP[10]) == 0 and int(campaign_price_color_IP[13]) == 0
"""
