from utilities.base_test import BaseTest
from utilities.loggers import log_message
from objects.login_page import LoginPage
from objects.shop_page import ShopPage
from objects.product_details_page import ProductDetailsPage


class CartTests(BaseTest):

    expected_price = "$30.00"

    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)
        self.shop_page = ShopPage(self.driver)
        self.product_details_page = ProductDetailsPage(self.driver)

    # Zadatak 1.6
    def test_adding_to_cart(self):
        log_message("Added products to cart")

        self.shop_page.navigate_to_page()

        # Navigating to /shop page
        self.shop_page.products_main_navigation.click()
        self.shop_page.products_main_navigation.click()
        self.shop_page.shop_main_navigation.click()

        # opening a physical product details page
        self.shop_page.physical_product.click()

        # opening a physical product details page
        self.shop_page.physical_product.click()

        # selecting the color and size
        self.product_details_page.choose_color.click()
        self.product_details_page.click_color(self.product_details_page.color_red)
        self.product_details_page.choose_dropdown_value.click()
        self.product_details_page.choose_size_dropdown.click()
        self.product_details_page.choose_dropdown_value.click()

        # adding another product (so we have 2 in total)
        self.product_details_page.plus_button.click()

        # adding the product to the cart
        self.product_details_page.add_to_cart_button.click()

        self.assertTrue(self.product_details_page.alert_snackbar)

        # opening the cart from the main navigation
        self.product_details_page.cart_button_navigation.click()

        total_price = self.product_details_page.total_price_label.text

        self.assertTrue(total_price == self.expected_price)
