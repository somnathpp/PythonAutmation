from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
# driver.find_element(By.LINK_TEXT,'Elements').click()
# winID=driver.current_window_handle
# print('win Id :',winID) # win Id : 112A636DF3E62707835378CCD68A46E7
#                         # win Id : 9B381807F405F395E1DBB943E3F87B89
# EVERY TIME WINDOW ID WILL DIFFERENT
# driver.find_element(By.LINK_TEXT,'Automation Testing').click()
driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()
IDS=driver.window_handles
pid=IDS[0] #parent window id
cid=IDS[1] #child window id
print('window id of parrent :',pid)
print('window id of child :',cid)
driver.switch_to.window(cid)
print('title of child window :',driver.title)
driver.switch_to.window(pid)
print('title of parent window :',driver.title)
time.sleep(20)