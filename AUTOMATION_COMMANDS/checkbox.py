from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)
#1 select only one radio button
# radioMale=driver.find_element(By.XPATH,"//input[@id='male']")
# radioMale.click()
#2 select Multiple radio buttons
# days=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# for day in days:
#     day.click()
# time.sleep(10)
#3 select radio as per choices
# days=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# for day in days:
#     ChoiceDay=day.get_attribute("id")
#     if ChoiceDay=="sunday" or ChoiceDay=="saturday" :
#      day.click()
#4 LAST TWO CHECK BOX SELECT
# days=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# for i in range(len(days)-2,len(days)):
#     days[i].click()
#
# time.sleep(10)
#5 FIRST TWO CHECK BOX SELECT
days=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# for i in range(0,len(days)):
#     if i<2:
#         days[i].click()
# time.sleep(5)
# #6 uncheck all
# days=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# for day in days:
#     if day.is_selected():
#         day.click()
# time.sleep(5)
