import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.get("https://artoftesting.com/samplesiteforselenium?utm_source=chatgpt.com")
driver.maximize_window()
ac=ActionChains(driver)
src=driver.find_element(By.ID,'myImage')
tgt=driver.find_element(By.ID,"targetDiv")
ac.drag_and_drop(src,tgt).perform()
time.sleep(15)