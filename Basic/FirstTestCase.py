'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

ser=Service(r"C:\drivers\edge\msedgedriver.exe")
driver = webdriver.Edge(service=ser)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.find_element(By.NAME,'username').send_keys('Admin')



time.sleep(25)
driver.quit()
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ser = Service(r"C:\drivers\edge\msedgedriver.exe")

driver = webdriver.Edge(service=ser)

driver.maximize_window()

driver.get("https://sauce-demo.myshopify.com/account/login")

wait = WebDriverWait(driver, 10)
#tag&id
# driver.find_element(By.CSS_SELECTOR,'input#customer_email').send_keys('abc')
# driver.find_element(By.CSS_SELECTOR,'#customer_email').send_keys('abc')
#tag&class
# driver.find_element(By.CSS_SELECTOR,'input.long').send_keys('abc')
driver.find_element(By.CSS_SELECTOR,'.long').send_keys('abc')
#tag&attribute
# driver.find_element(By.CSS_SELECTOR,'input[type=email]').send_keys('')
# driver.find_element(By.CSS_SELECTOR,'[type=email]').send_keys('')
#tag,class,attribute
driver.find_element(By.CSS_SELECTOR,'input.long[type="password"]').send_keys('abc')

# liknks=driver.find_elements(By.TAG_NAME,'a')
# print(len(liknks))
#driver.find_element(By.ID,"search-field").send_keys("jacket")
# cls=driver.find_elements(By.CLASS_NAME,"product")
# l=len(cls)
# print(l)
#driver.find_element(By.PARTIAL_LINK_TEXT ,"Sign").click()
#driver.find_element(By.ID,"search-submit").click()
#wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# driver.find_element(By.CSS_SELECTOR,'input#customer_email').send_keys('abc')
# driver.find_element(By.CSS_SELECTOR,'#customer_email').send_keys('abc')
driver.find_element(By.XPATH,'//*[@id=customer_email]').send_keys('abc')
driver.find_element(By.XPATH,'//*[@id=customer_password]').send_keys('123')
time.sleep(25)
driver.quit()
