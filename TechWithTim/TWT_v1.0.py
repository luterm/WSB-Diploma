from selenium import webdriver
from selenium.webdriver.common.by import By


import time


driver = webdriver.Chrome()
driver.get("https://google.com")
time.sleep(2)

reject_all_button = driver.find_element(By.ID, "W0wltc")
time.sleep(1)

reject_all_button.click()
time.sleep(3)

#now prepare a regular, automated search function in main google window
