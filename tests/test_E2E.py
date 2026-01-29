import json
import pytest

from pageObjects.Checkout import CheckoutPage
from pageObjects.Login import LoginPage
from pageObjects.Shop import ShopPage

test_data_path = "./data/test_data.json"
with open(test_data_path) as f:
    test_data = json.load(f)

@pytest.mark.smoke
@pytest.mark.parametrize("data",test_data)
def test_E2E(browser,data):
    driver = browser
    loginPage = LoginPage(driver)
    username = data["username"]
    password = loginPage.get_credentials(username)
    userDetails = data["userDetails"]
    shopPage = ShopPage(driver)
    checkutPage = CheckoutPage(driver)


    loginPage.login(username,password)
    shopPage.filter("lohi")
    shopPage.add_product_to_cart(data["productName"])
    shopPage.click_an_element(shopPage.cart)
    #checkutPage.click_an_element(checkutPage.remove(product_name))
    checkutPage.click_an_element(checkutPage.button_by_id("checkout"))
    checkutPage.delivery_details(userDetails["firstName"],userDetails["lastName"],userDetails["zipCode"])
    checkutPage.click_an_element(checkutPage.input_by_id("continue"))
    calculatedTotal,totalPrice = checkutPage.validate_bill()
    assert calculatedTotal == totalPrice

