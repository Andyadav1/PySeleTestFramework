from utils.Common import Common


class LoginPage(Common):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def login(self,username,password):
        self.driver.find_element(*self.input_by_id("user-name")).send_keys(username)
        self.driver.find_element(*self.input_by_id("password")).send_keys(password)
        self.driver.find_element(*self.input_by_id("login-button")).click()
