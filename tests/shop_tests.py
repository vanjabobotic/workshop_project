from utilities.base_test import BaseTest
from utilities.loggers import log_message
from objects.login_page import LoginPage
from objects.shop_page import ShopPage
from objects.product_details_page import ProductDetailsPage


class CartTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)
        self.shop_page = ShopPage(self.driver)
        self.product_details_page = ProductDetailsPage(self.driver)

    def test_adding_to_cart(self):
        log_message("Added products to cart")

        self.shop_page.navigate_to_page()

        self.shop_page.products_main_navigation.click()
        self.shop_page.products_main_navigation.click()
        self.shop_page.shop_main_navigation.click()

        self.shop_page.physical_product.click()
        self.product_details_page.choose_color.click()
        self.product_details_page.choose_dropdown_value.click()
        self.product_details_page.choose_size_dropdown.click()
        self.product_details_page.choose_dropdown_value.click()
        self.product_details_page.add_to_cart_button.click()

        self.product_details_page.wait_for_alert_snackbar()
        self.assertTrue(self.product_details_page.alert_snackbar)
