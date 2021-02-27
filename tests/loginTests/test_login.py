import pytest
from selenium import webdriver
from pathlib import *

class TestLogin:
    @pytest.fixture()
    def test_setup(self):
        global driver

        driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_login(self,test_setup):
        driver.get("https://parabank.parasoft.com/parabank/index.htm")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("demo")
        driver.find_element_by_name("password").submit()
        x = driver.title
        assert x == "ParaBank | Accounts Overview"

    def test_login_fail_test(self, test_setup):
        driver.get("https://parabank.parasoft.com/parabank/index.htm")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("demo")
        driver.find_element_by_name("password").submit()
        x = driver.title
        assert x == "xxxxxx"

    '''
    def test_teardown():
        driver.close()
        driver.quit()
        print("Test Completed")
    '''