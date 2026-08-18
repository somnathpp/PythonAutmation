from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)

drpcountry=Select(driver.find_element(By.XPATH,"//select[@id='country']"))
#selecting option  using the inbuilt functions
# drpcountry.select_by_visible_text('India')
# drpcountry.select_by_value('india')
# drpcountry.select_by_index(1)
time.sleep(5)
#capturing all options
allOptions=drpcountry.options
# print(len(allOptions))
# for option in allOptions:
#     print(option.text)
# #selecting option without using the inbuilt functions
# for option in allOptions:
#     if option.text=='India':
#         option.click()
# time.sleep(10)
# WITHOUT USING Select() class
all=driver.find_elements(By.XPATH,"//*[@id='country']/option")
print(len(all))
for option in all:
    print(option.text)