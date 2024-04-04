import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get("https://google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "W0wltc"))
)

reject_all_button = driver.find_element(By.ID, "W0wltc")
#time.sleep(1) 

reject_all_button.click()
time.sleep(1)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
#input_element.clear() - usefull in case of a 'search textbox' preloaded with any text in it
input_element.send_keys("glut ziarnisty" + Keys.ENTER)



breakpoint()


driver.quit()
#now prepare a regular, automated search function in main google window
