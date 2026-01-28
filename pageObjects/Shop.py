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
        self.cart = (By.XPATH,"//a[@class='shopping_cart_link']")


    def filter(self,selectFilter):
        filter = Select(self.driver.find_element(By.XPATH,"//select[@class='product_sort_container']"))
        filter.select_by_value(selectFilter)


    def add_product_to_cart(self,product_name):
        self.driver.find_element(*self.addProdsToCart(product_name)).click()


