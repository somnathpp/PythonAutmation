import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
driver.switch_to.frame('iframeResult')
txtB1=driver.find_element(By.XPATH,'//input[@id="field1"]')
txtB1.clear()
txtB1.send_keys("well come")

ac=ActionChains(driver)
btn=driver.find_element(By.XPATH,'/html/body/button')
ac.double_click(btn).perform()
time.sleep(15)
