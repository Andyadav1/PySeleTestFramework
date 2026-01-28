import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.Common import Common


class DeliveryPage(Common):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.continue_btn = self.click_an_element(self.input_by_id("continue"))
        self.cancel = self.click_an_element(self.button_by_id("cancel"))

    def delivery_details(self,firstName,lastName,zipCode):
        self.driver.find_element(*self.input_by_id("first-name")).send_keys(firstName)
        self.driver.find_element(*self.input_by_id("last-name")).send_keys(lastName)
        self.driver.find_element(*self.input_by_id("postal - code")).send_keys(zipCode)
