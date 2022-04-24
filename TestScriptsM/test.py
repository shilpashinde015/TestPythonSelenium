import allure
import allure_commons
import pytest
from selenium.webdriver import Chrome
import logging
import Utilities.loggerUtility as log_utils
from py.xml import html


class Testclass:
    log = log_utils.Logs_util(logging.INFO)

    def pytest_html_report_title(report):
        report.title = "TestReport for Website!"

    @pytest.fixture
    @pytest.hookimpl(tryfirst=True)
    def browserSetup(self):
        executable_path = "/home/shilpa/Downloads/chromedriver"
        driver = Chrome(executable_path)
        # Wait implicitly for elements to be ready before attempting interactions
        driver.implicitly_wait(10)
        return driver

    @allure.testcase("Test")
    def test_homepage(self, browserSetup):
        self.log.info("*************start**********")
        print("Hello")
        self.log.info("*************end**********")
        self.log("**************************")
# profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.folderList', 2)
# profile.set_preference('browser.download.manager.showWhenStarting', False)
# profile.set_preference('browser.download.dir', os.getcwd())
# profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/vnd.ms-excel'))
# profile.set_preference('general.warnOnAboutConfig', False)
# fire_path = "/usr/bin/firefox"
# executable_path = "/home/shilpa/Downloads/geckodriver"
# driver = webdriver.Firefox(executable_path)
# binary = FirefoxBinary(fire_path)
# driver = webdriver.Firefox(firefox_profile=profile,executable_path=executable_path)
# driver.get("https://www.google.com")
# executable_path = "/home/shilpa/Git/TestPythonSelenium/Utilities/chromedriver"
# # base_url = "https://www.google.com"
# os.environ["webdriver.chrome.driver"] = executable_path
# base_url = Readpropertyfile.getURL()
# driver = webdriver.Chrome(executable_path)
# print(base_url)
# driver.get('base_url')
# executable_path = "/home/shilpa/Git/TestPythonSelenium/Utilities/chromedriver"
# driver = webdriver.Chrome(executable_path)
#
# # URL of the website
# url_test = "https://www.geeksforgeeks.org/"
# url = Readpropertyfile.getURL()
# print(url)
# # Opening the URL
# driver.get(url)
#
# # Getting current URL
# get_url = driver.current_url
#
# # Printing the URL
# print(get_url)

# con = configparser.ConfigParser()
# con.read("/home/shilpa/Git/TestPythonSelenium/configFiles/config.ini")
# url = con.get("Information", "baseURL").replace('"','')
# print("url" + url)
# print(type(url))
# executable_path = "/home/shilpa/Git/TestPythonSelenium/Utilities/geckodriver"
# profile = webdriver.FirefoxProfile('/home/shilpa/.mozilla/firefox/2hscbyp5.default/')
# profile.set_preference("dom.webdriver.enabled", False)
# profile.set_preference('useAutomationExtension', False)
# profile.update_preferences()
# desired = DesiredCapabilities.FIREFOX
# driver = webdriver.Firefox(firefox_profile=profile,
#                            desired_capabilities=desired)
# test_url = "https://www.google.com/"
# if url is None or test_url is None:
#     print("Number of Same Characters: 0")
# print(len(url))
# print(len(test_url))
# size = min(len(url), len(test_url))  # Finding the minimum length
# count = 0  # A counter to keep track of same characters
# print("url")
# for i in range(len(url)):
#     print(url[i],end=" ")
#
# print("test_url")
# for i in range(len(test_url)):
#         print(test_url[i],end=" ")
# print("\n")
# for i in range(size):
#    # print(url[i])
#     if url[i] == test_url[i]:
#         #print(url[i])
#         count += 1  # Updating the counter when characters are same at an index
#
# print("Number of Same Characters:", count)
#
# if url == test_url:
#     print("same")
# executable_path = "/home/shilpa/Git/TestPythonSelenium/Utilities/chromedriver"
# driver = webdriver.Chrome(executable_path)
# driver.get(url)
