from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl as opx
from selenium.webdriver.support.select import Select
import XLUtils as x
file='C:\\Users\\admin\\Downloads\\dataFin.xlsx'
driver = webdriver.Edge()
driver.get('file:///C:/Users/admin/Downloads/fixed_deposit_calculator.html')
driver.maximize_window()
time.sleep(5)
rows=x.getRowCount(file,'s1')
for r in range(2,rows+1):
    pric=x.readData(file,'s1',r,1)
    roi=x.readData(file,'s1',r,2)
    pr1 = x.readData(file, 's1', r, 3)
    pr2 = x.readData(file, 's1', r, 4)
    frq = x.readData(file, 's1', r, 5)
    exp = x.readData(file, 's1', r, 6)
    driver.find_element(By.XPATH,'//input[@id="principal"]').send_keys(pric)
    driver.find_element(By.XPATH,'//input[@id="rate"]').send_keys(roi)
    driver.find_element(By.XPATH,'//input[@id="period"]').send_keys(pr1)
    prddrp=Select(driver.find_element(By.XPATH,'//select[@id="periodUnit"]'))
    prddrp.select_by_visible_text(pr2)
    frqdrp=Select(driver.find_element(By.XPATH,'//select[@id="frequency"]'))
    frqdrp.select_by_visible_text(frq)
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div[5]/button[1]').click()
    time.sleep(5)
    actl=driver.find_element(By.XPATH,'//div[@class="maturity-line"]/span[2]').text
    if float(exp)==float(actl):
        print('pass')
        x.writeData(file,'s1',r,8,'pass')
        x.fillGreenColor(file,'s1',r,8)
    else:
        print('fail')
        x.writeData(file,'s1',r,8,'fail')
        x.fillGreenColor(file,'s1',r,8)
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div[5]/button[2]').click()
    time.sleep(2)

