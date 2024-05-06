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

WebDriverWait(driver, 6).until(                                    
    EC.presence_of_element_located((By.CLASS_NAME, "fc-button-label"))
)                                                           

manage_options_button = driver.find_element(By.CLASS_NAME, "fc-button-label").click()

time.sleep(3)

WebDriverWait(driver, 6).until(
    EC.presence_of_element_located((By.ID, "langSelect-EN"))
)
lang_choice_but = driver.find_element(By.ID, "langSelect-EN").click()


#program data variables
cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

WebDriverWait(driver, 6).until(
    EC.presence_of_element_located((By.ID, cookie_id ))
)
cookie = driver.find_element(By.ID,cookie_id)

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
#    print(cookies_count)

    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i)).click()
            break

#