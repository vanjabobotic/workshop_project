from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductDetailsPage(BasePage):

    slug = ""

    def navigate_to_page(self):
        self.navigate(self.slug)

    select_product_color_locator = (
        By.CSS_SELECTOR,
        "[data-testid=product-page-select-color]",
    )
    choose_dropdown_element_locator = (By.CSS_SELECTOR, "[role='option']")
    choose_size_locator = (By.CSS_SELECTOR, "[data-testid=product-page-select-size]")
    add_to_cart_button_locator = (
        By.CSS_SELECTOR,
        "[data-testid=product-page-button-add-to-cart]",
    )
    alert_locator = (By.CSS_SELECTOR, "[role='alert']")

    @property
    def alert_snackbar(self):
        return self.get_present_element(self.alert_locator)

    def wait_for_alert_snackbar(self):
        self.wait_until_element_visible(self.alert_locator)

    @property
    def add_to_cart_button(self):
        return self.get_present_element(self.add_to_cart_button_locator)

    @property
    def choose_color(self):
        return self.get_present_element(self.select_product_color_locator)

    @property
    def choose_dropdown_value(self):
        return self.get_present_element(self.choose_dropdown_element_locator)

    @property
    def choose_size_dropdown(self):
        return self.get_present_element(self.choose_size_locator)
