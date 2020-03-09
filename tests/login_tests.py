from utilities.base_test import BaseTest
from utilities.loggers import log_message
from objects.login_page import LoginPage


class LoginTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)

    def test_login(self):
        log_message("Test case that tries to log in.")

        self.login_page.navigate_to_page()
        self.login_page.login_link.click()

        self.login_page.login_input_field.send_keys("TiersTiers")

        self.login_page.password_input_field.send_keys("LoopTest123")

        self.login_page.submit_button.click()
        self.login_page.save_screenshot("Log_in_process")

        self.assertTrue(self.login_page.navigation_profile_button)
