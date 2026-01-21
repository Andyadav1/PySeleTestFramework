import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from Login import LoginPage
from Shop import ShopPage


def test_E2E(browser):
    driver = browser
    driver.maximize_window()
    wait = WebDriverWait(driver,10)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    shop_page = login_page.login()
    shop_page.add_product_to_cart(product_name="Blackberry")
    checkout_page = shop_page.go_to_cart()
    checkout_page.checkout()







