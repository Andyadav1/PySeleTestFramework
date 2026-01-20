import pytest
from pygments.lexer import default
from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome", help="Choose your browser, default is Chrome"
    )

@pytest.fixture(scope="function")
def browser(request):
    browse_name = request.config.getoption("--browser_name")
    if browse_name == "Chrome":
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
    elif browse_name == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
    elif browse_name == "edge":
        driver = webdriver.Edge()
        driver.implicitly_wait(10)
    elif browse_name == "safari":
        driver = webdriver.Safari()
        driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)
    yield driver