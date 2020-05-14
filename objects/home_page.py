from utilities.base_page import *


class HomePage(BasePage):

    url_slug = ""

    def navigate_to_page(self):
        self.navigate(self.url_slug)