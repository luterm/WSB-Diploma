from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
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

# find and fill in login frame with the correct account name and password
# the following two lines doesn't work as they should - check out if 'send_keys' is implemented correctly
time.sleep(2)
username_txt = driver.find_element(By.NAME, "identifier")
username_txt.send_keys("some.username")


time.sleep(125)
# Close the driver
driver.quit()


#find example test cases to check login frame and password
#find an example of tests for collecting data from google search and collect them in a database created