from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

# Initialize Chrome driver instance
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

# Navigate to the url
driver.get("https://google.com")

rejection_button = driver.find_element(By.ID,"W0wltc")
#input_element.send_keys(Keys.ENTER)
def implicitly_wait(time_to_wait:int):
    
    time_to_wait(3)
    #driver.implicitly_wait(3)
    rejection_button.click(3)

time.sleep(5)

# Close the driver
driver.quit()  