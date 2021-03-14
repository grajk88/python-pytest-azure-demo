import pytest
from selenium import webdriver
from pathlib import *
from chromedriver_py import binary_path


class TestLogin:
    @pytest.fixture()
    def test_setup(self):
        try:
            global driver
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')

            driver = webdriver.Chrome(executable_path=binary_path, chrome_options=chrome_options)
            driver.implicitly_wait(10)
            driver.maximize_window()
            yield
            driver.close()
            driver.quit()
            print("Test Completed")
        except:
            print("Something is failing")

    def test_01_login(self, test_setup):
        try:
            driver.get("https://parabank.parasoft.com/parabank/index.htm")
            driver.find_element_by_name("username").send_keys("admin")
            driver.find_element_by_name("password").send_keys("demo")
            driver.find_element_by_name("password").submit()
            x = driver.title
            assert x == "ParaBank | Accounts Overview"
        except:
            print("Something is failing")
            assert False

    def test_02_login_fail_test(self, test_setup):
        try:
            driver.get("https://parabank.parasoft.com/parabank/index.htm")
            driver.find_element_by_name("username").send_keys("admin")
            driver.find_element_by_name("password").send_keys("demo")
            driver.find_element_by_name("password").submit()
            x = driver.title
            assert x == "ParaBank | Accounts Overview"
        except:
            print("Something Failed")
            assert False

    def test_03_login(self, test_setup):
        try:
            driver.get("https://parabank.parasoft.com/parabank/index.htm")
            driver.get_screenshot_as_base64()
            driver.find_element_by_name("username").send_keys("admin")
            driver.find_element_by_name("password").send_keys("demo")
            driver.find_element_by_name("password").submit()
            x = driver.title
            assert x == "ParaBank | Accounts Overview"
        except:
            print("Something is failing")
            assert False

    def test_04_login_fail_test(self, test_setup):
        try:
            driver.get("https://parabank.parasoft.com/parabank/index.htm")
            driver.find_element_by_name("username").send_keys("admin")
            driver.find_element_by_name("password").send_keys("demo")
            driver.find_element_by_name("password").submit()
            x = driver.title
            assert x == "ParaBank | Accounts Overview"
        except:
            print("Something is failing")
            assert False

    '''
    def test_teardown():
        driver.close()
        driver.quit()
        print("Test Completed")
    '''
