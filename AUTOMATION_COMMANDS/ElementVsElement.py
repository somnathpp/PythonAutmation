from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Edge()
driver.get('https://orangehrm.com/')
driver.maximize_window()
time.sleep(15)
# search=driver.find_element(By.XPATH,"//input[@placeholder='Username']")
# search.clear()
# search.send_keys("bag")
# print(search.get_attribute("value"))

footer=driver.find_elements(By.XPATH,"//div[@class='footer-main-section']//a")
print(len(footer))
for element in footer:
    print(element.text)
time.sleep(15)
driver.close()