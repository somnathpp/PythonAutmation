import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Edge()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,'//input[@id="dob"]').click()
time.sleep(5)
date='30'
datepicker_month=Select(driver.find_element(By.XPATH,'//select[@data-handler="selectMonth"]'))
datepicker_month.select_by_visible_text('Dec')
datepicker_year=Select(driver.find_element(By.XPATH,'//select[@data-handler="selectYear"]'))
datepicker_year.select_by_visible_text('2020')
dates=driver.find_elements(By.XPATH,'//table[@class="ui-datepicker-calendar"]/tbody/tr/td/a')
for dt in dates:
    if dt.text == date:
        dt.click()
        break
time.sleep(5)