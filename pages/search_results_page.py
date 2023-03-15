from locators.search_results_locators import SearchResultsLocators
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    def select_video_by_index(self, index):
        videos = self.elements_are_visible(SearchResultsLocators.VIDEOS_LIST)
        videos[index].click()
