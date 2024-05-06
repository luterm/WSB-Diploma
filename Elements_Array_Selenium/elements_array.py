from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.mediabiasfactcheck.com")

#WebDriverWait(driver, 3).until(                                  
#    EC.presence_of_element_located((By.ID, "W0wltc"))
#)                                                           

#reject_all_button = driver.find_element(By.ID, "W0wltc").click() 

#WebDriverWait(driver, 3).until(                                   #waiting for a 'searched phrase textbox' 
#    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
#)

#element = driver.find_element(By.CLASS_NAME, "gLFyf")
#element.send_keys("automated assertions tests python selenium vs code", Keys.ENTER)

#breakpoint()

    # Get element with tag name 'div'
element = driver.find_element(By.TAG_NAME, 'p')

    # Get all the elements available with tag name 'p'
elements = element.find_elements(By.TAG_NAME, 'p')
for e in elements:
    print(e.text)
  