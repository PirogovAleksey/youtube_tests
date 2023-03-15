from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.NAME, 'search_query')
    SEARCH_BUTTON = (By.ID, 'search-icon-legacy')
