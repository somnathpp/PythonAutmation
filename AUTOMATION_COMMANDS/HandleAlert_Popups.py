from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.get('https://mypage.rediff.com/login/dologin')
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='btnLogin']").click()
# driver.find_element(By.XPATH, '//button[@onclick="jsConfirm()"]').click()
# driver.find_element(By.XPATH, '//*[@onclick="jsPrompt()"]').click()
#switch to alert window
time.sleep(2)
driver.switch_to.alert.accept()
# alertWindow.send_keys('wellcome')
# alertWindow.dismiss()
time.sleep(5)
#Handle the Authentic Popup such as username and password
