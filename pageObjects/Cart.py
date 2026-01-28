from selenium.webdriver.common.by import By

from utils.Common import Common


class CartPage(Common):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.remove = lambda  product_name: (By.XPATH,f"//div[contains(text(),'{product_name}')]/../../../div/div/button")
        self.checkout = self.button_by_id("checkout")
        self.continue_shopping = self.button_by_id("continue-shopping")


    def remove_prodict(self,product_name):
        self.click_an_element(self.remove(product_name))
