import json

import pytest
from pygments.lexer import default
from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait

env_path = "data/env.json"
with open(env_path) as f:
    env = json.load(f)


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome", help="Choose your browser, default is Chrome"
    )

@pytest.fixture(scope="function")
def browser(request):
    browse_name = request.config.getoption("--browser_name")
    if browse_name == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options)
    elif browse_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options)
    elif browse_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(options)
    elif browse_name == "safari":
        options = webdriver.SafariOptions()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        driver = webdriver.Safari(options)

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)
    driver.get(env["url"])
    yield driver
    driver.close()