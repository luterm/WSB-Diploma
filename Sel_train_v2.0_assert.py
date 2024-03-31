from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://demostore.supersqa.com/my-account/")

username_txt_box = driver.find_element(By.ID, "username")
username_txt_box.send_keys("jujujujiuji")

password_txt_box = driver.find_element(By.ID, "password")
password_txt_box.send_keys("piopipopipopipiop")

login_button = driver.find_element(By.NAME, "login").click()

expected_msg = "Error: The username jujujujiuji is not registered on this site. If you are unsure of your username, try your email address instead."


#repair the By.XPATH invalid synthax problem - resolved; by 'copy full XPath' instead of 'copy XPath'

err_msg_box = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/ul/li") 
displayed_err = err_msg_box.text

assert displayed_err == expected_msg, "Displayed error is not as expected."

print("PASS")


breakpoint()