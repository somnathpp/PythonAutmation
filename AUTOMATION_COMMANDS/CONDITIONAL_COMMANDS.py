from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
ser_obj=Service(r'C:\drivers\edge\msedgedriver.exe')
driver=webdriver.Edge(service=ser_obj)

# driver.get("https://sauce-demo.myshopify.com/")
# searchbox=driver.find_element(By.XPATH,'//input[@id="search-field"]')
# print('display_status :',searchbox.is_displayed())
# print('enable_status :',searchbox.is_enabled())
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
searradio1=driver.find_element(By.XPATH,'//input[@id="male"]')
searradio2=driver.find_element(By.XPATH,'//input[@id="female"]')
print('Status Before Male RadioButton Selected : ',searradio1.is_selected())
print('Status Before FeMale RadioButton Selected :',searradio2.is_selected())
searradio1.click()
print('Status After Male RadioButton Selected :',searradio1.is_selected())
time.sleep(5)
driver.quit()
