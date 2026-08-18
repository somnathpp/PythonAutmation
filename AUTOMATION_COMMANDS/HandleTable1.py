from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(5)

# Find rows
rows = driver.find_elements(
    By.XPATH,
    '//table[@name="BookTable"]//tr'
)

# Find columns
columns = driver.find_elements(
    By.XPATH,
    '//table[@name="BookTable"]//tr/th'
)

NR = len(rows)
NC = len(columns)

print("Number of Rows:", NR)
print("Number of Columns:", NC)

for r in range(2, NR + 1):
    for c in range(1, NC + 1):

        desire = driver.find_element(
            By.XPATH,
            f'//table[@name="BookTable"]/tbody/tr[{r}]/td[{c}]'
        )

        print(desire.text)