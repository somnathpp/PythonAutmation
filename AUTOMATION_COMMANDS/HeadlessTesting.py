from selenium import webdriver
def headless_edge():
    ops=webdriver.EdgeOptions()
    ops.add_argument("--headless")
    # ops.add_argument("--disable-gpu")
    driver = webdriver.Edge(options=ops)
    return driver
driver=headless_edge()
driver.get("https://the-internet.herokuapp.com/")
print(driver.title)
print(driver.current_url)
driver.close()