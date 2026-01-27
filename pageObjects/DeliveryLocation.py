import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.Common import Common


class DeliveryPage(Common):
    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)
        self.search_country_name = (By.XPATH,"//input[contains(@id,'country')]")
        self.suggested_country = lambda country_name : (By.XPATH,f"//div[@class='suggestions']//a[contains(text(),'"+country_name+"')]")
        self.purchase = (By.XPATH,"//input[contains(@class,'btn-success')]")

    def delivery_location(self,CountryName):
        self.driver.find_element(*self.search_country_name).send_keys(CountryName)
        wait = WebDriverWait(self.driver, 10)

        wait.until(expected_conditions.visibility_of_element_located(self.suggested_country(CountryName)))
        select_country =  self.driver.find_element(*self.suggested_country(CountryName))
        select_country.click()
        time.sleep(5)
        #if select_country.is_displayed():
        select_country.click()
        self.driver.find_element(*self.purchase).click()

    def validation(self):
        success_text = "Success! Thank you! Your order will be delivered in next few weeks :-)."
        success = self.driver.find_element(By.XPATH,"//div/strong[text()='Success!']/../../div")
        print(success.text)
        print(success_text)
        #assert success.text == success_text
