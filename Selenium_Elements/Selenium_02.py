from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

# Initialize Chrome driver instance
driver = webdriver.Chrome

# Navigate to the url
driver.get("https://google.com")

# Wait for some time to ensure the page is fully loaded
time.sleep(3)

# Find the rejection button
rejection_button = driver.find_element(By.ID, "W0wltc")

# Wait for 3 seconds before clicking the button
time.sleep(3)
rejection_button.click()

time.sleep(5)
# Close the driver
driver.quit()


#add this file to git loc repo and check oyt github config and synchro
#find example test cases to check login frame and password
#find an example of tests for collecting data from google search and collect them in a database created
#check out the new git tool on desktop and config it