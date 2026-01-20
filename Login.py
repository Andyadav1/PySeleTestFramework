from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username = (By.XPATH,"//input[@id='username']")
        self.password = (By.XPATH, "//input[@id='password']")
        self.signin = (By.XPATH,"//input[@id='signInBtn']")

    def login(self):
        self.driver.find_element(*self.username).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password).send_keys("Learning@830$3mK2")
        self.driver.find_element(*self.signin).click()
