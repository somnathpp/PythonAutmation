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
print(driver.title)
print(driver.current_url)
print(driver.page_source)
