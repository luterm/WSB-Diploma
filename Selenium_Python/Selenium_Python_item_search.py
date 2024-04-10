from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com/")

search_id = "woocommerce-product-search-field-0"
search_elements = driver.find_element(By.ID, search_id)
search_elements.send_keys("Nikie Boobs")
search_elements.send_keys(Keys.ENTER)
# upon a shortened ver merging two code lines into one search_elements.send_keys("Nikie Boots")

expected_text = "No products were found matching your selectiown."
message_locator = '//*[@id="main"]/p'
message_element = driver.find_element(By.XPATH, message_locator)
displayed_text = message_element.text

assert displayed_text == expected_text, f"The expected text did not show up." \
f"Expected: {expected_text}" \
f"Actual: {displayed_text}"
print("PASS")

#breakpoint()