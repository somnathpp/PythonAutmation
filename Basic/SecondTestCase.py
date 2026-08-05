from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ser = Service(r"C:\drivers\edge\msedgedriver.exe")
driver=webdriver.Edge(service=ser)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
wait=WebDriverWait(driver,10)

wait.until(EC.visibility_of_element_located((By.NAME,'username'))).send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
driver.quit()



