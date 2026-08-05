from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Edge()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT,"Udemy Courses").click()
# time.sleep(5)
# driver.find_element(By.PARTIAL_LINK_TEXT,"Udemy").click()
# time.sleep(5)
links=driver.find_elements(By.XPATH,"//a")
print(len(links))
time.sleep(2)
for link in links:
    print(link.text," :", link.get_attribute("href"))

