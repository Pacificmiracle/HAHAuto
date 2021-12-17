import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
# Open Website
driver.get("http://18.136.220.168:1001/auth/login")
#driver.get_screenshot_as_file("abcdtest.png") #samedirectory

time.sleep(2)
# Enter in Email Or Mobile Number
email_mobile = driver.find_element_by_xpath("//input[@placeholder='Email or Mobile No.']")
email_mobile.send_keys("sabin.maharjan@abc.com")
# Enter in Password
Password = driver.find_element_by_xpath("//input[@placeholder='Password']")
Password.send_keys("test")
# Click on Login
Login = driver.find_element_by_xpath("//button[normalize-space()='Login']")
Login.click()

# Click on Unread Message
unreadmsg = driver.find_element(By.XPATH,"/a[@ng-reflect-router-link='/messages']//div[@class='box1']")
unreadmsg.click()
time.sleep(2)

# Click on Notifications
notifications = driver.find_element(By.XPATH,"//a[@ng-reflect-router-link='/notifications']//h3")
notifications.click()
time.sleep(2)

# Click On Patients
patients = driver.find_element(By.XPATH,"//a[@ng-reflect-router-link='/patients']//h3")
notifications.click()
time.sleep(2)

# Click on Lab Bookings
labbookings = driver.find_element(By.XPATH,"//a[@ng-reflect-router-link='/lab-bookings']//h3")
labbookings.click()
time.sleep(2)

#Click on My Appointment
myappointment = driver.find_element(By.XPATH,"//a[@ng-reflect-router-link='/my-appointment']//h3")
myappointment.click()
time.sleep(2)

print(driver.current_url)
print(driver.title)
