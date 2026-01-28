import json
from unittest import expectedFailure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

creds = "./data/loginData.json"
with open(creds) as f:
    users = json.load(f)


class Common:
    def __init__(self,driver):
        self.driver = driver
        self.input_by_id = lambda id_text: (By.XPATH,f"//input[@id='{id_text}']")
        self.button_by_id = lambda id_text: (By.XPATH,f"//button[@id='{id_text}']")




    def get_title(self):
        self.driver.title()

    def waitForClickable(self,locator,timeout):
        wait = WebDriverWait(self.driver,timeout)
        wait.until(expected_conditions.element_to_be_clickable(locator))


    def click_an_element(self,locator):
        self.waitForClickable(locator,10)
        self.driver.find_element(*locator).click()


    def get_credentials(self,username):
        for user in users.values():
            if user["username"] == username:
                return user["password"]
        return None

