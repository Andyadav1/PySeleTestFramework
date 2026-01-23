from selenium.webdriver.common.by import By


class Common:
    def __init__(self,driver):
        self.driver = driver
        self.input_by_id = lambda id_text : (By.XPATH,f"//input[@id='{id_text}']")

    def get_title(self):
        self.driver.title()
