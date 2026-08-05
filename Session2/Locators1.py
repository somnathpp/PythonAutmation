from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import time
serv=Service(r'C:\drivers\edge\msedgedriver.exe')
driver=webdriver.Edge(service=serv)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
wait = WebDriverWait(driver, 10)
driver.maximize_window()
wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(25)
driver.quit()