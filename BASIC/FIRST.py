"""
Make sure to install:
    pip install selenium webdriver-manager
Automates login to a website using Selenium in Python.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import sys

# ---------- CONFIGURATION ----------
LOGIN_URL = "https://portal.vmedulife.com/public/auth/#/login/rgip-hasegaon"  # Replace with actual login page URL
USERNAME = "FCRGIP2430"               # Replace with your username
PASSWORD = "Potdar@15"               # Replace with your password
USERNAME_FIELD_ID = "username"           # Replace with actual HTML ID or name
PASSWORD_FIELD_ID = "password"           # Replace with actual HTML ID or name
LOGIN_BUTTON_SELECTOR = "button[type='submit']"  # CSS selector for login button
TIMEOUT = 10  # seconds
# -----------------------------------

def login_to_website():
    try:
        # Setup Chrome WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        # Open login page
        driver.get(LOGIN_URL)

        # Wait for username field
        WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.ID, USERNAME_FIELD_ID))
        )

        # Enter username
        username_field = driver.find_element(By.ID, USERNAME_FIELD_ID)
        username_field.clear()
        username_field.send_keys(USERNAME)

        # Enter password
        password_field = driver.find_element(By.ID, PASSWORD_FIELD_ID)
        password_field.clear()
        password_field.send_keys(PASSWORD)

        # Click login button
        login_button = driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON_SELECTOR)
        login_button.click()

        # Wait for successful login (example: wait for dashboard element)
        WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))  # Change to a real element after login
        )

        print("✅ Login successful!")
        return driver  # Keep browser open for further automation

    except TimeoutException:
        print("❌ Timeout: Page took too long to load or element not found.")
    except NoSuchElementException:
        print("❌ Error: Could not find one of the required elements.")
    except WebDriverException as e:
        print(f"❌ WebDriver error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    driver_instance = login_to_website()
    # driver_instance.quit()  # Uncomment to close browser after login