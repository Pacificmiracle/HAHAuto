class Homepage():

    def __init__(self, driver):
        self.driver = driver

        self.profile_class = "img-circle image-circle-active image-style"
        self.logout_link_xpath = "/html/body/div[1]/app-root/app-header/nav/ul[2]/li/a/i"

    def click_profile(self):
        self.driver.find_element_by_class(self.profile_class).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()

    
