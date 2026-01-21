from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self,driver):
        self.driver = driver
        self.checkout_button = (By.XPATH,"//button[contains(text(),'Checkout')]")


    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        delivey_page = Deli(self.driver)



