from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class ShopPage(BasePage):

    slug = ""
    products_main_navigation_locator = (
        By.CSS_SELECTOR,
        "[data-testid=main-navigation-products]",
    )
    shop_main_navigation_locator = (
        By.CSS_SELECTOR,
        "[data-testid=main-navigation-shop]",
    )
    physical_product_locator = (
        By.CSS_SELECTOR,
        "[data-testid='shop-product-[TEST] Physical Product']",
    )
    software_product_locator = (
        By.CSS_SELECTOR,
        "[data-testid='shop-product-[TEST] Software Product']",
    )
    choose_color_product_locator = (
        By.CSS_SELECTOR,
        "[data-testid=product-page-select-color]",
    )

    def navigate_to_page(self):
        self.navigate(self.slug)

    @property
    def products_main_navigation(self):
        return self.get_visible_element(self.products_main_navigation_locator)

    @property
    def shop_main_navigation(self):
        return self.get_visible_element(self.shop_main_navigation_locator)

    @property
    def physical_product(self):
        return self.get_present_element(self.physical_product_locator)

    @property
    def software_product(self):
        return self.get_present_element(self.software_product_locator)
