import json


import pytest

from pageObjects.Cart import CartPage
from pageObjects.Checkout import CheckoutPage
from pageObjects.Login import LoginPage
from pageObjects.Shop import ShopPage
from utils.Common import users

test_data_path = "./data/test_data.json"
with open(test_data_path) as f:
    test_data = json.load(f)

@pytest.mark.smoke
@pytest.mark.parametrize("data",test_data)
def test_E2E(browser,data):
    driver = browser
    loginPage = LoginPage(driver)
    password = loginPage.get_credentials(data["UserName"])
    shopPage = ShopPage(driver)
    cartPage = CartPage(driver)

    loginPage.login(data["UserName"],password)
    shopPage.filter("lohi")
    shopPage.add_product_to_cart(data["ProductName"])
    shopPage.click_an_element(shopPage.cart)
    cartPage.remove_prodict(data["ProductName"])
    cartPage.click_an_element(cartPage.checkout)



