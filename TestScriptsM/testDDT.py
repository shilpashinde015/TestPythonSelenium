import os.path
import allure
from Utilities.readProperties import Readpropertyfile
from PageObjectModel.LoginPage import LoginPage
from selenium.webdriver import Chrome
import pytest
import logging
import Utilities.loggerUtility as log_utils
import Utilities.XLUtils as xu


@allure.title("ToolsQA TestSuite")
class Test_Homepage:
    dir_path = "/home/shilpa/Git/TestPythonSelenium/Screenshots/"
    baseUrl = Readpropertyfile.getURL().replace('"', '')
    log = log_utils.Logs_util(logging.INFO)
    XL_path = "/home/shilpa/Git/TestPythonSelenium/TestData/Data.xlsx"

    # fill_cell3 = PatternFill(patternType='solid', fgColor='35FC03')

    @allure.step("Home page Testcases")
    @pytest.fixture
    def browserSetup(self):
        executable_path = "/home/shilpa/Downloads/chromedriver"
        driver = Chrome(executable_path)
        # Wait implicitly for elements to be ready before attempting interactions
        driver.implicitly_wait(10)
        return driver

    @allure.testcase("Login Credentials Test")
    def test_login_credentials(self, browserSetup):

        self.log.info("****Credential Test case***")
        self.driver = browserSetup
        self.driver.get(self.baseUrl)
        self.logp = LoginPage(self.driver)
        self.rows = xu.getRowCount(self.XL_path, 'Sheet1')
        print(self.rows)

        for r in range(2, self.rows + 1):
            self.uName = xu.readData(self.XL_path, 'Sheet1', r, 1)
            self.passwd = xu.readData(self.XL_path, 'Sheet1', r, 2)
            self.result = xu.readData(self.XL_path, 'Sheet1', r, 3)
            print(self.uName)
            print(self.passwd)

            self.logp.setUname(self.uName)
            self.logp.setPassword(self.passwd)
            self.logp.click_Login()
            account_val = self.driver.find_element_by_xpath(self.logp.account_name).text
            print("accountName: " + account_val)

            if account_val == "admin":
                self.log.info("**** Login Succesful ****")
                self.driver.save_screenshot(os.path.join(self.dir_path, "login.png"))
                self.result == 'Pass'
                # self.result = self.fill_cell3
                self.driver.close()
                assert True
            else:
                self.log.error("**** Login failed****")
                self.driver.save_screenshot(os.path.join(self.dir_path, "login.png"))
                self.driver.close()
                assert False
