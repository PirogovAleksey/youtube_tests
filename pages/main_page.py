from selenium.webdriver.common.keys import Keys
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def fill_search_form_and_submit(self, search_query):
        self.element_is_clickable(MainPageLocators.SEARCH_FIELD).send_keys(search_query)
        self.element_is_clickable(MainPageLocators.SEARCH_BUTTON).send_keys(Keys.ENTER)
