from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_visible_in_dom(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_not_visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))