from selenium import webdriver
import time
import unittest
# LOGIN & LOGOUT UNITTEST
class LoginTest(unittest.TestCase):
    @classmethod

    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        # Open Website
        self.driver.get("http://18.136.220.168:1001/auth/login")
        time.sleep(2)

        # Enter in Email Or Mobile Number
        email_mobile = self.driver.find_element_by_xpath("//input[@placeholder='Email or Mobile No.']")
        email_mobile.send_keys("sabin.maharjan@abc.com")
        # Enter in Password
        Password = self.driver.find_element_by_xpath("//input[@placeholder='Password']")
        Password.send_keys("test")
        # Click on Login
        Login = self.driver.find_element_by_xpath("//button[normalize-space()='Login']")
        Login.click()

        # Click on Logout
        Logout = self.driver.find_element_by_xpath("/html/body/div[1]/app-root/app-header/nav/ul[2]/li/a/i")
        time.sleep(2)
        Logout.click()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")






