from utilities.base_test import BaseTest
from utilities.loggers import log_message
from objects.login_page import LoginPage
from utilities import constants


class LoginTests(BaseTest):

    username_correct_validation_message = "Username or E-mail is required!"
    password_correct_validation_message = "Password is required!"

    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)

    def test_success_login(self):
        log_message("Successful login.")

        self.login_page.navigate_to_page()
        self.login_page.login_link.click()

        self.login_page.login_input_field.send_keys(constants.VALID_USERNAME)
        self.login_page.password_input_field.send_keys(constants.VALID_PASSWORD)
        self.login_page.submit_button.click()
        self.login_page.navigation_profile_button.click()

        self.login_page.save_screenshot("Log_in_process")

        navigation_profile_name_label = self.login_page.navigation_profile_button_username.text

        self.assertTrue(navigation_profile_name_label == constants.VALID_USERNAME)

    def test_failed_login(self):
        log_message("Failed login.")

        self.login_page.navigate_to_page()
        self.login_page.login_link.click()

        self.login_page.submit_button.click()

        username_error_label = self.login_page.username_validation_message
        password_error_label = self.login_page.password_validation_message

        self.login_page.save_screenshot("Log_in_process_validation_message")

        self.assertTrue(username_error_label.text == self.username_correct_validation_message)
        self.assertTrue(password_error_label.text == self.password_correct_validation_message)
