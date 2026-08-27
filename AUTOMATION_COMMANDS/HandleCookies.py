import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/download?utm_source=chatgpt.com")
driver.maximize_window()
cookies=driver.get_cookies()
print('Before adding cookie :',len(cookies))
# for c in cookies:
#     # print(c)
#     print(c.get('name')," :",c.get('expiry'))
time.sleep(5)
#add new cookie
driver.add_cookie({'name':'My Cookie','value':'12345','Gen':'men'})
cookies=driver.get_cookies()
print('After adding new cookie :',len(cookies))
# delete one cookie
driver.delete_cookie('My Cookie')
cookies=driver.get_cookies()
print('After deleting  one cookie :',len(cookies))
time.sleep(5)
# delete all cookie
driver.delete_all_cookies()
cookies=driver.get_cookies()
print('After deleting all cookies  :',len(cookies))