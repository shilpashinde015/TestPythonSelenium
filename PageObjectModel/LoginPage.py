class LoginPage:
    uname_id = "userName"
    passid = "password"
    login_btn = "//*[@id='login']"
    account_name = '//*[@id="userName-value"]'
    #accont_name = '//*[text()="admin"]'

    def __init__(self, driver):
        self.driver = driver

    def setUname(self, uName):
        self.driver.find_element_by_id(self.uname_id).clear()
        self.driver.find_element_by_id(self.uname_id).send_keys(uName)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.passid).clear()
        self.driver.find_element_by_id(self.passid).send_keys(password)

    def click_Login(self):
        self.driver.find_element_by_xpath(self.login_btn).click()

    def check_account_name(self):
        self.account_name



