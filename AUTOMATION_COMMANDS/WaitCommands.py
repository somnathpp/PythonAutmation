import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotInteractableException
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Edge()
mywait=WebDriverWait(driver,20,poll_frequency=2,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotInteractableException])     #explicit Wait decleration
driver.get('https://www.google.com/')
driver.maximize_window()
# searchBox=driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
searchBox=mywait.until(EC.presence_of_element_located((By.XPATH,"//textarea[@id='APjFqb']")))
searchBox.send_keys('selenium')
searchBox.submit()
time.sleep(15)
searchs=mywait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='VuuXrf']")))
searchs.click()
time.sleep(30)

# //span[@class='VuuXrf']