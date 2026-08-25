import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://text-compare.com/")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(5)
input1=driver.find_element(By.XPATH,'//textarea[@id="inputText1"]')
input2=driver.find_element(By.XPATH,'//textarea[@id="inputText2"]')
act=ActionChains(driver)
input1.send_keys("hi how are you")
time.sleep(5)
# ctrl+A
act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# ctrl+C
act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
# tab
act.send_keys(Keys.TAB).perform()

# ctrl+v
act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
time.sleep(5)

