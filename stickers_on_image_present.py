import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_all_images_have_sticker(driver):
    driver.get("http://localhost/litecart/")
    products_list = driver.find_elements_by_css_selector(('.product'))
    for i in range(0, len(products_list)):
        product_sticker = products_list[i].find_elements_by_css_selector("[class^='sticker ']")
        if len(product_sticker) == 1:
            print('Product %s contains one sticker' % (i + 1))
        elif len(product_sticker) < 1:
            print('There is not sticker for product %s' % (i + 1))
        else:
            print('Product %s contains more than one sticker' % (i + 1))
