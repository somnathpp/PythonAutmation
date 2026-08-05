import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver = webdriver.Edge()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
time.sleep(5)
AllLinks=driver.find_elements(By.TAG_NAME,'a')
count=0
for link in AllLinks:
    url=link.get_attribute('href')
    if url is None:
        continue

    try:
        res = requests.head(url, allow_redirects=True, timeout=15)
    except:
       None



    if res.status_code>=400:
        print(url,'  is broken  link')
        count+=1
    else:
        print(url,'  is valid  link')

print('Broken Links :',count)
print('Valid Links :',len(AllLinks)-count)