import os.path
import allure
from Utilities.readProperties import Readpropertyfile
from PageObjectModel.LoginPage import LoginPage
from selenium.webdriver import Chrome
import pytest
import logging
import Utilities.loggerUtility as log_utils


@allure.title("ToolsQA TestSuite")
class Test_Homepage:
    dir_path = "/home/shilpa/Git/TestPythonSelenium/Screenshots/"
    baseUrl = Readpropertyfile.getURL().replace('"', '')
    userName = Readpropertyfile.getUsername()
    password = Readpropertyfile.getPassword()
    log = log_utils.Logs_util(logging.INFO)

    @allure.step("Home page Testcases")
    @pytest.fixture
    def browserSetup(self):
        executable_path = "/home/shilpa/Downloads/chromedriver"
        driver = Chrome(executable_path)
        # Wait implicitly for elements to be ready before attempting interactions
        driver.implicitly_wait(10)
        return driver

    @allure.testcase("Homepage Title Test")
    def test_homepage(self, browserSetup):
        self.log.info("*************** test_homepage *****************")
        self.log.info("****Started Home page title test ****")
        self.driver = browserSetup
        self.driver.get(self.baseUrl)
        try:
            self.driver.get(base_url)
        except Exception as e:
            print("except -> browser.get -> %s" % e)

        actual_title = self.driver.title
        print("actual_title: " + actual_title)

        if actual_title == "ToolsQA":
            self.log.info("**** Home page title test passed ****")
            self.driver.save_screenshot(os.path.join(self.dir_path, "title.png"))
            self.driver.close()
            assert True
        else:
            self.log.error("**** Home page title test failed****")
            self.driver.save_screenshot(os.path.join(self.dir_path, "title.png"))
            # self.sc_shot.take_screenshots("homepageTest.png")
            self.driver.close()
            assert False

    @allure.testcase("Login Credentials Test")
    def test_login_credentials(self, browserSetup):

        self.log.info("****Credential Test case***")
        self.driver = browserSetup
        self.driver.get(self.baseUrl)
        self.logp = LoginPage(self.driver)
        self.logp.setUname(self.userName)
        self.logp.setPassword(self.password)
        self.logp.click_Login()
        account_val = self.driver.find_element_by_xpath(self.logp.account_name).text
        print("accountName: " + account_val)

        if account_val == "admin":
            self.log.info("**** Login Succesful ****")
            self.driver.save_screenshot(os.path.join(self.dir_path, "login.png"))
            self.driver.close()
            assert True
        else:
            self.log.error("**** Login failed****")
            self.driver.save_screenshot(os.path.join(self.dir_path, "login.png"))
            self.driver.close()
            assert False
