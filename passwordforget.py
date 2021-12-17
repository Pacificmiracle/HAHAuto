import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://18.136.220.168:1001/auth/login")
#driver.get_screenshot_as_file("abcdtest.png") #samedirectory

time.sleep(2)
# Click On Forget Password
forget_password = driver.find_element_by_xpath("//a[normalize-space()='Forgot Password']")
forget_password.click()

# Enter In Email
fpemail = driver.find_element_by_xpath("//input[@placeholder='Email']")
fpemail.send_keys("prashant.test@yopmail.com")

# Click on "Send Reset Link"
sendbtn = driver.find_element_by.xpath("//button[normalize-space()='Send Reset Link']")
sendbtn.click()

print(driver.current_url)
print(driver.title)

