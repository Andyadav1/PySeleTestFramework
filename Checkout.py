from selenium.webdriver.common.by import By

from DeliveryLocation import DeliveryPage
from utils.Common import Common


class CheckoutPage(Common):
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)
        self.checkout_button = (By.XPATH,"//button[contains(text(),'Checkout')]")


    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        delivey_page = DeliveryPage(self.driver)
        return delivey_page
