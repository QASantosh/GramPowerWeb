class LoginPage():

#locators of all the element
    username_textbox_xpath = "//input[@name='username']"
    password_textbox_xpath = "//input[@name='password']"
    login_button_xpath = "//input[@value='LOG IN']"

#Create the constructor to initialize the driver
    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def setPassword(self, password):
            self.driver.find_element_by_xpath(self. password_textbox_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
