from utilities.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException


class ProductDetailsPage(BasePage):

    slug = ""

    def navigate_to_page(self):
        self.navigate(self.slug)

    select_product_color_locator = (By.CSS_SELECTOR, "[data-testid=product-page-select-color]")
    choose_dropdown_element_locator = (By.CSS_SELECTOR, "[role='option']")
    choose_size_locator = (By.CSS_SELECTOR, "[data-testid=product-page-select-size]")
    add_to_cart_button_locator = (By.CSS_SELECTOR, "[data-testid=product-page-button-add-to-cart]")
    alert_locator = (By.CSS_SELECTOR, "[role='alert']")
    plus_button_locator = (By.CSS_SELECTOR, "[data-testid=product-page-quantity-button-plus]")
    main_navigation_cart_button_locator = (By.CSS_SELECTOR, "[data-testid=main-navigation-cart]")
    total_price_locator = (By.CSS_SELECTOR, "[data-testid=cart-info-total-price]")
    size_elements_locator = (By.CSS_SELECTOR, "[role='option']")
    color_elements_locator = (By.CSS_SELECTOR, "[role='option']")

    color_green = "Green"
    color_red = "Red"
    size_S = "S"
    size_M = "M"
    size_L = "L"

    def click_color(self, color):
        try:
            color_elements = self.get_present_elements(self.color_elements_locator)

            for element in color_elements:
                if element.text == color:
                    element.click()

        except StaleElementReferenceException:
            pass

    def click_size(self, size):
        try:
            size_elements = self.get_present_elements(self.size_elements_locator)

            for element in size_elements:
                if element.text == size:
                    element.click()

        except StaleElementReferenceException:
            pass

    @property
    def total_price_label(self):
        return self.get_present_element(self.total_price_locator)

    @property
    def cart_button_navigation(self):
        return self.get_present_element(self.main_navigation_cart_button_locator)

    @property
    def plus_button(self):
        return self.get_present_element(self.plus_button_locator)

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
