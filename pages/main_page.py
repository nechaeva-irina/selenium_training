from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_main_page(self):
        self.driver.get("http://localhost/litecart/")
        return self

    def select_item(self):
        self.driver.find_elements_by_css_selector('img[class="image"]')[0].click()
        return self