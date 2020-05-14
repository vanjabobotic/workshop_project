from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class FeedPage(BasePage):

    slug = "/en-us/feed"

    feed_meta_locator = (By.CSS_SELECTOR, "meta[name='page-name'][content='feed']")
    feed_main_navigation_locator = (By.CSS_SELECTOR, "[data-testid=main-navigation-feed]'")

    def navigate_to_page(self):
        self.navigate(self.slug)

    @property
    def feed_main_navigation(self):
        return self.get_visible_element(self.feed_main_navigation_locator)

    @property
    def feed_meta_name(self):
        return self.get_present_element(self.feed_meta_locator)
