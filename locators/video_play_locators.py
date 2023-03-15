from selenium.webdriver.common.by import By


class VideoPlayLocators:
    SKIP_ADS = (By.CLASS_NAME, 'ytp-ad-skip-button-container')
    VIDEO_SLIDER = (By.CSS_SELECTOR, '.ytp-progress-bar-container')
