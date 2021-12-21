# POM for Login
# from Page_Objects.Locators.weblocators import Locators
class LoginPage():
    def __init__(self, driver):

        self.driver = driver
        self.email_mobile_textbox_xpath = "//input[@placeholder='Email or Mobile No.']"
        self.password_textbox_xpath = "//input[@placeholder='Password']"
        self.login_btn_xpath = "//button[normalize-space()='Login']"

    def enter_email_mobile(self, email_mobile):
        self.driver.find_element_by_xpath(self.email_mobile_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.email_mobile_textbox_xpath).sendkeys("sabin.maharjan@logicabeans.com")

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).sendkeys("test")

    def click_login(self, login):
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()



