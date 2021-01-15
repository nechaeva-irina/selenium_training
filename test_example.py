import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from datetime import date
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)
    def after_find(self, by, value, driver):
        print(by, value, "found")
    def on_exception(self, exception, driver):
        print(exception)
        today = str(date.today())
        driver.get_screenshot_as_file('screen' + today + '.png')
        print()


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name('q').send_keys('webdriver', Keys.ENTER)
    WebDriverWait(driver,10).until(EC.title_is('webdriver - Поиск в Google'))
    for l in driver.get_log("browser"):
        print(l)
