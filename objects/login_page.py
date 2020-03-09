from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    slug = ""
    login_link_locator = (By.XPATH, "//a[@class='css-5rd2ea']")
    login_input_field_locator = (By.CSS_SELECTOR, "[data-testid=login-username-field]")
    password_input_field_locator = (By.CSS_SELECTOR, "[data-testid=login-password-field]")
    submit_button_locator = (By.CSS_SELECTOR, "[data-testid=login-submit-button]")
    navigation_profile_locator = (By.CSS_SELECTOR, "[data-testid=main-navigation-profile]")

    def navigate_to_page(self):
        self.navigate(self.slug)

    @property
    def login_link(self):
        return self.get_present_element(self.login_link_locator)

    @property
    def login_input_field(self):
        return self.get_present_element(self.login_input_field_locator)

    @property
    def password_input_field(self):
        return self.get_present_element(self.password_input_field_locator)

    @property
    def submit_button(self):
        return self.get_present_element(self.submit_button_locator)

    @property
    def navigation_profile_button(self):
        return self.get_present_element(self.navigation_profile_locator)

