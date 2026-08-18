import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,'//input[@id="datepicker"]').click()
time.sleep(5)
#select month and year
date='30'
month='March'
year='2020'

while True:
    mn = driver.find_element(By.XPATH, '//*[@class="ui-datepicker-month"]').text
    yr = driver.find_element(By.XPATH, '//*[@class="ui-datepicker-year"]').text
    if mn==month and yr==year:
        break
    else:
        # driver.find_element(By.XPATH,'//*[@data-handler="next"]').click()     # for future year
        driver.find_element(By.XPATH, '//*[@data-handler="prev"]').click() # for past year

time.sleep(5)
dates=driver.find_elements(By.XPATH, '//table[@class="ui-datepicker-calendar"]/tbody/tr/td/a')
for dt in dates:
   if dt.text == date:
       dt.click()
       break
time.sleep(5)