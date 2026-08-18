from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
ops=Options() 
ops.add_argument('--disable-notifications')
pref={ "profile.default_content_setting_values.geolocation": 2 } #1 :Allow  2:Block

ops.add_experimental_option( "prefs",pref)
driver = webdriver.Edge(options=ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window()
time.sleep(5)
