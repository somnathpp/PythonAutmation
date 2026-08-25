import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
time.sleep(5)
min_slider=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
max_slider=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')
print('Location  of min and max slider : ')
print('min_slider Location before :',min_slider.location)
print('max_slider Location before :',max_slider.location)
time.sleep(5)
act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-65,0).perform()
print('Location  of min and max slider : ')
print('min_slider Location after :',min_slider.location)
print('max_slider Location after :',max_slider.location)
time.sleep(15)
