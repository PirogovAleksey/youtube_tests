import time

from selenium.webdriver import ActionChains

from locators.video_play_locators import VideoPlayLocators
from pages.base_page import BasePage


class VideoPlayPage(BasePage):
    def skip_ads(self):
        while True:
            try:
                self.element_is_clickable(VideoPlayLocators.SKIP_ADS, 10).click()
            except:
                break

    def drag_video(self):
        slider = self.element_is_visible_in_dom(VideoPlayLocators.VIDEO_SLIDER)
        actions = ActionChains(self.driver)
        actions.move_to_element(slider).click().perform()

    def pause_video(self):
        time.sleep(10)
        actions = ActionChains(self.driver)
        actions.send_keys('K')
        actions.perform()
