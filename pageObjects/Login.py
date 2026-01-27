from utils.Common import Common
from pageObjects.Shop import ShopPage


class LoginPage(Common):
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    def login(self,Username,Password):
        self.driver.find_element(*self.input_by_id("user-name")).send_keys(Username)
        self.driver.find_element(*self.input_by_id("password")).send_keys(Password)
        self.driver.find_element(*self.input_by_id("login-button")).click()
        shop_page = ShopPage(self.driver)
        return shop_page
