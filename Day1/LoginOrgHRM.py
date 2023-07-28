# import controller as controller
# import keyboard as keyboard
# from select import select
#from controller import controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from pynput.keyboard import Key, Controller
#from.selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.select import Select

serv_obj = Service('"C:\Drivers\chromedriver_win32 \chromedriver.exe"')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')

driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
#time.sleep(3)
driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']").click()
#time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys("Raj96kkk")

driver.find_element(By.XPATH,"//div[@class='oxd-select-text-input']").click()
driver.find_element(By.XPATH,"//span[text()='ESS']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("Rakesh")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
driver.find_element(By.XPATH,"//span[text()='Enabled']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
driver.find_element(By.XPATH,"//span[text()='class='oxd-checkbox-input oxd-checkbox-input--active --label-right oxd-checkbox-input']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//span[normalize-space()='Job']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//a[normalize-space()='Job Titles']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
driver.find_element(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys("Test1")
time.sleep(2)
driver.find_element(By.XPATH,"//textarea[@placeholder='Type description here']").send_keys('Selenium With Python')
#driver.find_element(By.XPATH,"//input[@type='file']").send_keys("C:/Users/raj96/PycharmProjects/pythonpro/Files/Screenshot (23).png")
driver.find_element(By.XPATH,"//input[@type='file']").send_keys("C:/Users/raj96/Pictures/Screenshots/Screenshot (86).png")
time.sleep(2)
driver.find_element(By.XPATH,"//textarea[@placeholder='Add note']").send_keys('Hello')
#time.sleep(5)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)











# drp_admin=select(driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"))
# #drp_downlist=driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']").click()
# time.sleep(2)
#driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]").click()

# driver.refresh()
#time.sleep(5)
#
#admin_ele=driver.find_element(By.XPATH,"//div[@class='oxd-select-text-input'][normalize-space()='Admin']")
#admin_ele=driver.find_element(By.XPATH,"///div[@class='oxd-select-text-input'][normalize-space()='Admin']")


# admin_drp=Select(admin_ele)
#
# admin_drp.select_by_visible_text('Admin')
#
# time.sleep(5)
# # driver.find_element(By.XPATH,"//div[@class='oxd-select-text-input']").click()
# driver.refresh()
# driver.implicitly_wait(4)
# driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active']").click()
# driver.implicitly_wait(4)
# #driver.find_element("//span[@class='oxd-chip oxd-chip--default orangehrm-password-chip']")