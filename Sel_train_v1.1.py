from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

# Initialize Chrome driver instance
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

# Navigate to the url
driver.get("https://google.com")

# Wait for 'n'sec to ensure the page is fully loaded
time.sleep(1)

# Find the rejection_button
rejection_button = driver.find_element(By.ID, "W0wltc")

# Wait for 'n' sec, then click the rejection_button
time.sleep(2)
rejection_button.click()

# wait for 'n'sec, then push sign_in_button
time.sleep(1)
sign_in_button = driver.find_element(By.CLASS_NAME, "gb_Kd")
sign_in_button.click()


time.sleep(10)
# Close the driver
driver.quit()


#find example test cases to check login frame and password
#find an example of tests for collecting data from google search and collect them in a database created
#check out the new git tool on desktop and config it