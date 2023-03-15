from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.video_play_page import VideoPlayPage


class TestSearch:
    def test_search_and_play(self, driver):
        main_page = MainPage(driver, 'https://www.youtube.com/')
        search_results_page = SearchResultsPage(driver, 'https://www.youtube.com/')
        video_play_page = VideoPlayPage(driver, 'https://www.youtube.com/')
        main_page.open()
        main_page.fill_search_form_and_submit('Bossa Nova')
        search_results_page.select_video_by_index(1)
        video_play_page.skip_ads()
        video_play_page.drag_video()
        video_play_page.pause_video()
