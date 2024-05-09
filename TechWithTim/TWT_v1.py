import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://google.com")

WebDriverWait(driver, 3).until(                                     # does it work same way as the 'implicit wait'?
    EC.presence_of_element_located((By.ID, "W0wltc"))
)                                                           

reject_all_button = driver.find_element(By.ID, "W0wltc").click()    # '.click()' instead of the next code line, literally : 'reject_all_button.click()'
time.sleep(2)

WebDriverWait(driver, 3).until(                                     # waiting for a 'searched phrase input frame'
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")         # assigning the 'searched phrase input frame' to an object, to be used in furhter operations
#input_element.clear() - usefull in case of a 'searched phrase input frme' preloaded with any text in it by default

input_element.send_keys("automated assertions tests python selenium vs code", Keys.ENTER) #assigning exact text to be written in the 'searched phrase input frame'
time.sleep(2)

#breakpoint()

WebDriverWait(driver, 3).until(
    EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "testing in"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "testing in").click()

time.sleep(2)

#to search for all the elements including a certain phrase use this:
#links = driver.find_elements(By.PARTIAL_LINK_TEXT, "gluty") #it should return an array of results, how to make it?
#[element1, element2, element3]

#breakpoint()
driver.quit()