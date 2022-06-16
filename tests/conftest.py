import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        #"--cmdopt", action="store", default="type1", help="my option: type1 or type2"
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome("C:\chromedriver\chromedriver_win32 (2)\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    #driver.close()

    #elif browser_name == "firefox":
        #pass
    #elif browser_name == "IE":
        #pass


