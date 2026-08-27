import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os



location=os.getcwd()
def edge_setup():
    # prefernce={'download.default_directory':location}
    ops=webdriver.EdgeOptions()
    # ops.add_experimental_option('prefs',prefernce)
    driver=webdriver.Edge()
    return driver
driver=edge_setup()
# driver.get("https://the-internet.herokuapp.com/download?utm_source=chatgpt.com")
# driver.maximize_window()
# driver.find_element(By.XPATH,'//*[@id="content"]/div/a[24]').click()
# time.sleep(25)
# def chrome_setup():
#     prefernce={'download.default_directory':location}
#     ops=webdriver.ChromeOptions()
#     ops.add_experimental_option('prefs',prefernce)
#     driver=webdriver.Chrome(options=ops)
#     return driver
# driver=chrome_setup()
# driver.get("https://the-internet.herokuapp.com/")
# driver.maximize_window()
# driver.find_element(By.XPATH,'//*[@id="content"]/div/a[24]').click()
# time.sleep(25)
# def firefox_setup():
#     ops = webdriver.FirefoxOptions()
#     ops.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/msword')
#     ops.set_preference('browser.download.manager.showWhenStarting', False)
#     ops.set_preference('browser.download.folderList', 2)#0-desktop,1-default 2-desired
#     ops.set_preference('browser.download.dir', location)
#     driver=webdriver.Firefox(options=ops)
#     return driver
# driver=firefox_setup()
driver.get("https://the-internet.herokuapp.com/download?utm_source=chatgpt.com")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="content"]/div/a[24]').click()
time.sleep(25)
