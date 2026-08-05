from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ser_obj = Service(r'C:\drivers\edge\msedgedriver.exe')
driver=webdriver.Edge(service=ser_obj)
driver.get('https://demoqa.com/')
driver.maximize_window()
print(driver.title)
driver.find_element(By.XPATH,"//img[@alt='Selenium Online Training']")



time.sleep(5)

driver.close()
