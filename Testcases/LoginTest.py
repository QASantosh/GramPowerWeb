import unittest
import HtmlTestRunner
from selenium import webdriver

from Pages.LoginPage import LoginPage
import time

class loginTest(unittest.TestCase):
    baseUrl = "https://data.grampower.com/hes/"
    username = "parul"
    password = "grampower"

    def Testcase1(self):
        self.driver = webdriver.Chrome("/home/parul/santoshworkspace/chromedriver_linux64/chromedriver")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))