from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service('"C:\Drivers\chromedriver_win32 \chromedriver.exe"')
driver = webdriver.Chrome(service=serv_obj)

driver.get('http://dosmartqa.stagsoftware.net:3009/login')
driver.maximize_window()
#time.sleep(2)
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Ramki")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Raj96kali@")
time.sleep(5)
driver.find_element(By.XPATH,"//button[@id='login-form-submit']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='Create app']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder='Enter application name']").send_keys("SmartQA1 ")
# #time.sleep(5)
driver.find_element(By.XPATH,"//textarea[@placeholder='Enter application details']").send_keys('QA Test Tool1')
time.sleep(5)
driver.find_element(By.XPATH,"//div[@id='application']//div[@class='h-100']//div//div//button[@class='form-submit-button'][normalize-space()='Add']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[@class='text-color-white active']").click()
driver.find_element(By.XPATH,"//div[@class='dropdown open']//div[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 dropdown-item'][normalize-space()='SmartQA1']").click()
driver.find_element(By.XPATH,"//div[@id='createNew']//div[@class='h-100']//div//div//button[@class='form-submit-button'][normalize-space()='Add']").click()
time.sleep(5)

# #breakpoint()
# driver.find_element(By.XPATH,"//a[normalize-space()='Create project']").click()
# #driver.find_element(By.XPATH,"//button[@aria-expanded='false']//div[@class='row strict']").click()
#
# driver.find_element(By.XPATH,"//button[@aria-expanded='true']//span[contains(text(),'ZOHO inventory')]").click()
# driver.find_element(By.XPATH,"//div[@class='dropdown open']//div[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 dropdown-item'][normalize-space()='DoSmartQA']").send_keys('DoSmartQA')
# time.sleep(5)
