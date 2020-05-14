from utilities.base_test import BaseTest
from utilities.loggers import log_message
from objects.login_page import LoginPage
from objects.feed_page import FeedPage
from objects.home_page import HomePage


class NavigationTests(BaseTest):

    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)
        self.feed_page = FeedPage(self.driver)
        self.home_page = HomePage(self.driver)

    def test_feed_navigation_page(self):
        log_message("Testing feed navigation")

        self.home_page.navigate_to_page()
        self.feed_page.feed_main_navigation.click()

        self.assertTrue(self.feed_page.feed_meta_name)
