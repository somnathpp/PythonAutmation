from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Edge()

driver.get("https://demo.automationtesting.in/Frames.html#google_vignette")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'Iframe with in an Iframe').click()

time.sleep(5)
# outerFrame=driver.find_element(By.XPATH,'//*[@id="singleframe"]')
# driver.switch_to.frame(outerFrame)
# innerFrame = driver.find_element(By.XPATH, "//iframe[@name='SingleFrame']")
# driver.switch_to.frame(innerFrame)
# driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("abc")
time.sleep(15)
