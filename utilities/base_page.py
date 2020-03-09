from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utilities import config
from utilities import constants
from utilities.loggers import log_message
from utilities.loggers import log_screenshot
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import time
from abc import ABC, abstractmethod


class BasePage(ABC):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # NAVIGATION

    @abstractmethod
    def navigate_to_page(self):
        pass

    def navigate(self, url_slug):
        self.driver.get(config.base_url + url_slug)

    # FETCHING

    def get_present_element(self, locator_value, timeout=constants.DRIVER_TIMEOUT):
        condition = expected_conditions.presence_of_element_located
        return self.__get_element(locator_value, condition, timeout)

    def get_visible_element(self, locator_value, timeout=constants.DRIVER_TIMEOUT):
        condition = expected_conditions.visibility_of_element_located
        return self.__get_element(locator_value, condition, timeout)

    def get_invisible_element(self, locator_value, timeout=constants.DRIVER_TIMEOUT):
        condition = expected_conditions.invisibility_of_element_located
        return self.__get_element(locator_value, condition, timeout)

    def get_present_elements(self, locator_value, timeout=constants.DRIVER_TIMEOUT):
        condition = expected_conditions.presence_of_all_elements_located
        return self.__get_elements(locator_value, condition, timeout)

    # FETCHING - PRIVATE

    def __get_element(self, locator_value, expected_condition, timeout):
        locator = locator_value[0]
        value = locator_value[1]
        condition = expected_condition

        try:
            element: WebElement = WebDriverWait(self.driver, timeout).until(
                condition((locator, value))
            )
            return element

        except Exception:
            log_message("Getting {} failed".format(value))

    def __get_elements(self, locator_value, expected_condition, timeout):
        locator = locator_value[0]
        value = locator_value[1]
        condition = expected_condition

        try:
            elements: [WebElement] = WebDriverWait(self.driver, timeout).until(
                condition((locator, value))
            )
            return elements

        except Exception:
            log_message("Getting {} failed".format(value))

    # WAIT

    def wait_until_element_present(
        self, locator_value, timeout=constants.DRIVER_TIMEOUT
    ):
        self.__wait_until(
            locator_value, expected_conditions.presence_of_element_located, timeout
        )

    def wait_until_element_visible(
        self, locator_value, timeout=constants.DRIVER_TIMEOUT
    ):
        self.__wait_until(
            locator_value, expected_conditions.visibility_of_element_located, timeout
        )

    def wait_until_element_invisible(
        self, locator_value, timeout=constants.DRIVER_TIMEOUT
    ):
        self.__wait_until(
            locator_value, expected_conditions.invisibility_of_element_located, timeout
        )

    def wait_until_title_matches(self, title, timeout=constants.DRIVER_TIMEOUT):
        condition = expected_conditions.title_is
        WebDriverWait(self.driver, timeout).until(condition(title))

    # WAIT - PRIVATE

    def __wait_until(self, locator_value, expected_condition, timeout):
        locator = locator_value[0]
        value = locator_value[1]
        WebDriverWait(self.driver, timeout).until(expected_condition((locator, value)))

    # VALIDATION

    def is_title_matching(self, expected_title, timeout=constants.DRIVER_TIMEOUT):
        condition = expected_conditions.title_is

        try:
            WebDriverWait(self.driver, timeout).until(condition(expected_title))
            return True

        except Exception:
            return False

    # INTERACTION

    def hover_over_element(self, element):
        try:
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()

        except Exception:
            log_message("Hovering on {} failed".format(element))

    # JAVASCRIPT

    def browser_go_back(self):
        try:
            self.driver.execute_script("window.history.go(-1)")

        except Exception:
            log_message("Going back failed")

    def scroll_to_element(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

        except Exception:
            log_message("Scrolling to {} failed".format(element))

    def set_local_storage_key(self, key, value):
        try:
            self.driver.execute_script(
                "window.localStorage.setItem({}, {});".format(key, value)
            )

        except Exception:
            log_message("Setting local storage key failed")

    # HELPERS

    def save_screenshot(self, title):
        timestamp = str(int(time.time()))
        image_name = title + "_" + timestamp + ".png"
        image_path = constants.SCREENSHOT_DIR + image_name

        try:
            self.driver.save_screenshot(image_path)
            log_screenshot(image_path)

        except Exception:
            log_message("Saving screenshot failed")
