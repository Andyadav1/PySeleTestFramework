from selenium.webdriver.common.by import By

from Commons import Commons
from Shop import ShopPage


class LoginPage(Commons):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def login(self):
        self.driver.find_element(*self.input_by_id("username")).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.input_by_id("password")).send_keys("Learning@830$3mK2")
        self.driver.find_element(*self.input_by_id("signInBtn")).click()
        shop_page = ShopPage(self.driver)
        return shop_page
