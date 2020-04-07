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

        # self.login_page.login_link.click()
        # self.login_page.login_input_field.send_keys(constants.TEST_VALID_USERNAME)
        # self.login_page.password_input_field.send_keys(constants.TEST_VALID_PASSWORD)
        # self.login_page.submit_button.click()

        self.shop_page.products_main_navigation.click()
        self.shop_page.products_main_navigation.click()
        self.shop_page.shop_main_navigation.click()

        self.shop_page.physical_product.click()

        self.assertTrue(self.product_details_page.choose_color)
