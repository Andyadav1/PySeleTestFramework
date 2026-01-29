
from selenium.webdriver.common.by import By
from utils.Common import Common


class CheckoutPage(Common):
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)
        self.remove = lambda  product_name: (By.XPATH,f"//div[contains(text(),'{product_name}')]/../../../div/div/button")

    def delivery_details(self,firstName,lastName,zipCode):
        self.driver.find_element(*self.input_by_id("first-name")).send_keys(firstName)
        self.driver.find_element(*self.input_by_id("last-name")).send_keys(lastName)
        self.driver.find_element(*self.input_by_id("postal-code")).send_keys(zipCode)


    def validate_bill(self):
        taxstr = self.driver.find_element(*self.div_by_class("summary_tax_label")).text
        tax = float(taxstr.split("Tax: $")[1])
        prices = self.driver.find_elements(*self.div_by_class("inventory_item_price"))
        total = self.driver.find_element(*self.div_by_class("summary_total_label")).text
        totalPrice = float(total.split("Total: $")[1])

        totalAmount = 0
        for price in prices:
            amountStr = price.text
            cleanAmount = float(amountStr.split("$")[1])
            totalAmount = totalAmount + cleanAmount

        calculatedTotal = totalAmount + tax
        calculatedTotal = round(calculatedTotal, 2)
        return calculatedTotal,totalPrice



