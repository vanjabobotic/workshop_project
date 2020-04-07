from utilities.base_test import BaseTest
from utilities.loggers import log_message
from objects.login_page import LoginPage
from utilities import constants


class LoginTests(BaseTest):

    username_correct_validation_message = "Username or E-mail is required!"

    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)

    def test_success_login(self):
        log_message("Success login.")

        self.login_page.navigate_to_page()
        self.login_page.login_link.click()

        self.login_page.login_input_field.send_keys(constants.TEST_VALID_USERNAME)
        self.login_page.password_input_field.send_keys(constants.TEST_VALID_PASSWORD)
        self.login_page.submit_button.click()

        self.login_page.save_screenshot("Log_in_process")

        self.assertTrue(self.login_page.navigation_profile_button)

    def test_failed_login(self):
        log_message("Failed login.")

        self.login_page.navigate_to_page()
        self.login_page.login_link.click()

        self.login_page.password_input_field.send_keys(constants.TEST_INVALID_PASSWORD)
        self.login_page.submit_button.click()

        username_error_label = self.login_page.username_validation_message

        self.login_page.save_screenshot("Log_in_process_validation_message")

        self.assertTrue(
            username_error_label.text == self.username_correct_validation_message
        )
