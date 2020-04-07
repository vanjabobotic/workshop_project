from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductDetailsPage(BasePage):

    slug = ""
    select_product_color_locator = (
        By.CSS_SELECTOR,
        "[data-testid=product-page-select-color]",
    )

    def navigate_to_page(self):
        self.navigate(self.slug)

    @property
    def choose_color(self):
        return self.get_present_element(self.select_product_color_locator)
