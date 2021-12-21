from selenium import webdriver
import time
import unittest

# Separate TestScripts and Objects

from Page_Objects.Pages.LoginPage import LoginPage
from Page_Objects.Pages.Homepage import Homepage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):

        self.driver.get("http://18.136.220.168:1001/auth/login")
        time.sleep(2)

        login = LoginPage(self.driver)
        login.enter_email_mobile("sabin.maharjan@abcd.com")
        login.enter_password("test")
        login.click_login()

        homepage = Homepage(self.driver)
        homepage.click_profile()
        homepage.click_logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")









