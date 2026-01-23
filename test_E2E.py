import json

import pytest

from Login import LoginPage
test_data_path = "./data/test_data.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    data_lists = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("data",data_lists)
def test_E2E(browser,data):
    driver = browser
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    shop_page = login_page.login(data["UserName"],data["Password"])
    shop_page.add_product_to_cart(product_name=data["ProductName"])
    checkout_page = shop_page.go_to_cart()
    delivery_page = checkout_page.checkout()
    delivery_page.delivery_location(CountryName="Ind")
    delivery_page.validation()






