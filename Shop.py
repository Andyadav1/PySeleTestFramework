from mimetypes import add_type

from selenium.webdriver.common.by import By

from Checkout import CheckoutPage
from utils.Common import Common


class ShopPage(Common):
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)
        self.shopTab = (By.XPATH,"//a[text()='Shop']")
        self.productCards = (By.XPATH,"//div[@class='card h-100']")
        self.productName = (By.XPATH,"div/h4/a")
        self.addToCart = (By.XPATH,"div/button")
        self.checkoutTab = (By.XPATH,"//a[contains(text(),' Checkout')]")


    def add_product_to_cart(self,product_name):
        self.driver.find_element(*self.shopTab).click()
        products = self.driver.find_elements(*self.productCards)
        for product in products:
            ProductName = product.find_element(*self.productName).text
            if ProductName == product_name:
                product.find_element(*self.addToCart).click()
                break


    def go_to_cart(self):
        self.driver.find_element(*self.checkoutTab).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page