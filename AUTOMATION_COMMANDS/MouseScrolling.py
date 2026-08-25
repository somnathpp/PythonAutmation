from  selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Edge()
driver.get("http://countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(5)
act=webdriver.ActionChains(driver)
# 1 scroll down by certain pixel without using Actionchain() class obj old method b4 2022
# driver.execute_script("window.scrollBy(0,2000)"," ")
# value=driver.execute_script("return window.pageYOffset")
# print('Number of pixel moved down : ',value)
# time.sleep(5)
# 1 scroll down by certain pixel using Actionchain() class obj new method after 2022 selenium 4.2

act.scroll_by_amount(0,2000).perform()
time.sleep(5)
#2 Scroll down till the element is found old method b4 2022
# IndFlag=driver.find_element(By.XPATH,'//*[@id="ct-list"]/table[1]/tbody/tr[86]/td[1]/img')
# driver.execute_script("arguments[0].scrollIntoView();",IndFlag)
# value=driver.execute_script("return window.pageYOffset;")
# print('pixel position after get Indian flag :',value)
# time.sleep(5)
#2 Scroll down till the element is found new method after 2022
IndFlag=driver.find_element(By.XPATH,'//*[@id="ct-list"]/table[1]/tbody/tr[86]/td[1]/img')
act.scroll_to_element(IndFlag).perform()
time.sleep(5)
# 3 scroll down till the last page position old method b4 2022
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(5)
# value=driver.execute_script("return window.pageYOffset;")
# print('pixel position after go to last  :',value)
# 3 scroll down till the last page position new method after 2022
footr=driver.find_element(By.ID,'footer')
act.scroll_to_element(footr).perform()
time.sleep(5)

# 4 scroll down till the start page position
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
# time.sleep(5)
# value=driver.execute_script("return window.pageYOffset;")
# print('pixel position after go to start position :',value)