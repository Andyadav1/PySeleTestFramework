from mimetypes import add_type

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.Checkout import CheckoutPage
from utils.Common import Common


class ShopPage(Common):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.addProdsToCart = lambda productName : (By.XPATH,f"//div[contains(text(),'{productName}')]/../../../div/button")
        self.checkoutTab = (By.XPATH,"//span[@class='select_container']")


    def filter(self):
        filter = Select(self.driver.find_element(By.XPATH,"//select[@class='product_sort_container']"))
        filter.select_by_value("")




    def add_product_to_cart(self,product_name):
        self.driver.find_element(*self.addProdsToCart(product_name)).click()


    def go_to_cart(self):
        self.driver.find_element(*self.checkoutTab).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page