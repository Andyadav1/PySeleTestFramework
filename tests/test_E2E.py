import json


import pytest

from pageObjects.Login import LoginPage
test_data_path = "./data/test_data.json"
with open(test_data_path) as f:
    test_data = json.load(f)

@pytest.mark.smoke
@pytest.mark.parametrize("data",test_data)
def test_E2E(browser,data):
    driver = browser
    login_page = LoginPage(driver)
    password = login_page.get_credentials(data["UserName"])
    shop_page = login_page.login(data["UserName"],password)
    shop_page.click_an_element(shop_page.addProdsToCart("Backpack"))
    shop_page.add_product_to_cart(product_name=data["ProductName"])
    checkout_page = shop_page.go_to_cart()
    delivery_page = checkout_page.checkout()
    delivery_page.delivery_location(CountryName="Ind")
    delivery_page.validation()



