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
) #does it work the way as 'implicit wait' works?

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

    #to search the link by an included text form the 'text search'
    #check with a text which differs from the 'search phrase'
WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "glut"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "glut")
    #to search an exact text; use LINK_TEXT, without PARTIAL alias before
    #it addressess to the first link met expected text search condition
link.click()

    #to search for all the elements including a certain phrase use this:
#links = driver.find_elements(By.PARTIAL_LINK_TEXT, "gluty") #it should return an array of results, how to make it?
#[element1, element2, element3]




breakpoint()


driver.quit()
#now prepare a regular, automated search function in main google window
