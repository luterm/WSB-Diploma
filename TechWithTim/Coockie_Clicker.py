from selenium import webdriver
#from selenium.webdriver.chrome.service import Service #check if this is neccessary!
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#service = Service(executable_path="chromedrivercostam")

driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/cookieclicker/")
    #add automated coockies rejection by finding all the switches for 'legitimate interess' and turn them off
    #is there a method to automatically detect such switches on any website by the global element of that type characteristics?

WebDriverWait(driver, 3).until(                                    
    EC.presence_of_element_located((By.CLASS_NAME, "fc-button-label"))
)                                                           

manage_options_button = driver.find_element(By.CLASS_NAME, "fc-button-label").click()

time.sleep(3)

WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.ID, "langSelect-EN"))
)
lang_choice_but = driver.find_element(By.ID, "langSelect-EN").click()
breakpoint()


breakpoint()