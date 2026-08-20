import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
btn=driver.find_element(By.XPATH,'/html/body/main/p/span')
ac=ActionChains(driver)
ac.context_click(btn).perform()

time.sleep(15)