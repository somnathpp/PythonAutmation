from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
# serv_obj=Service(r"C:\drivers\edge\msedgedriver.exe")
driver=webdriver.Edge()
driver.get('https://www.snapdeal.com/')
driver.maximize_window()
time.sleep(5)
driver.get('https://www.amazon.in/')
driver.maximize_window()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.close()