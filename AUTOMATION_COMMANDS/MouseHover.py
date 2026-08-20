import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.get('https://seleniumbase.io/demo_page?utm_source=chatgpt.com')
driver.maximize_window()
time.sleep(5)
ac=ActionChains(driver)
HD1=driver.find_element(By.ID,'myDropdown')
link1=driver.find_element(By.XPATH,'//a[@id="dropOption1"]')
# link2=driver.find_element(By.ID,'//a[@id="dropOption2"]')
# link3=driver.find_element(By.ID,'//a[@id="dropOption3"]')
ac.move_to_element(HD1).move_to_element(link1).click().perform()
# ac.move_to_element(link2).click()
time.sleep(5)