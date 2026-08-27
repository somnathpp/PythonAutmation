from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/upload?utm_source=chatgpt.com")
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@id="file-upload"]').send_keys('C:\\Users\\admin\\Documents\\FIRST YEAR\\11.pdf')
driver.find_element(By.XPATH,'//input[@class="button"]').click()
time.sleep(12)
