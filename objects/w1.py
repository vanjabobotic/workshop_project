from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from time import sleep


browser = webdriver.Chrome()

browser.get("https://www.infinum.com/the-capsized-eight")

shameless_link: WebElement = WebDriverWait(browser, 10).until(
    expected_conditions.presence_of_element_located((By.LINK_TEXT, "Shameless"))
)
shameless_link.click()

sleep(10)

browser.quit()
