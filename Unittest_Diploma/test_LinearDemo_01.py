import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#Class Create

class LinearDemo(unittest.TestCase):

    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def test_linear_flow_testing_01(self):
        # Navigate to desired web page and verify web page is displayed
        self.driver.get("https://jignect.tech/")
        self.assertTrue("Software and QA Testi ng Company| JigNect Technologies Pvt Ltd" in self.driver.title, "Expected text not found in page title")
        
         # Click on the contact us button
        contact_us_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/nav/ul/li[8]/a").click() 
       
        # Verify desired page i displayed
        contact_us_header = self.driver.find_element(By.CSS_SELECTOR, "div[class='contact-title'] h2").text
        self.assertEqual(contact_us_header, "Let's talk", "Contact Us page does not displayed")

        # Generate random string
        full_name = "".join(random.choice(string.ascii_letters) for _ in range(11))

        # Enter value in full name and company name, select checkbox and click on submit button
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Full name']").send_keys(full_name)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Company']").send_keys("Bulepa")
        time.sleep(3)
        
        self.driver.find_element(By.CSS_SELECTOR, "span[id='checkboxOne']").click()
        #breakpoint()
    
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()

        #verify the validation message for mandatory fields
        expected_validation_message = 'The field is required.'

        textarea_actual_validation_message = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(2) > div > p > span > span").text # Changed to actual
        
        email_actual_validation_message = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(3) > div:nth-child(2) > p > span > span").text # Changed to actual
        
        phone_number_actual_validation_message = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(4) > div:nth-child(2) > p > span > span").text # Changed to actual


        self.assertEqual(textarea_actual_validation_message, expected_validation_message, "textarea validation message does not match")

        self.assertEqual(email_actual_validation_message, expected_validation_message, "Email validation message does not match")

        self.assertEqual(phone_number_actual_validation_message, expected_validation_message, "Phone number validation message does not match")


# It is mandatory when you want to run code using command prompt
#if __name__ == '__main__':
#    unittest.main()

# Why does it work under Pythest and Unittest as well?
# Why __init__ file in the project folder is no longer required?


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import string
import unittest

class ContactFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("URL_OF_YOUR_FORM")  # Replace with the actual URL

    def tearDown(self):
        self.driver.quit()

    def test_company_field_interactive(self):
        characters = string.ascii_letters + string.digits
        company_name = "".join(random.choice(characters) for _ in range(12))
        company_field = self.driver.find_element(By.XPATH, '//*[@id="contact-new-form"]/div[4]/div[1]/p/span/input')
        company_field.send_keys(company_name)
        time.sleep(3)
        company_field_value = company_field.get_attribute("value")
        self.assertEqual(company_field_value, company_name, "Expected user input not present in 'Company' field")

    def test_work_email_field_clickable(self):
        work_email_xpath = '//*[@id="contact-new-form"]/div[3]/div[2]/p/span/input'
        work_email_field = self.driver.find_element(By.XPATH, work_email_xpath)
        try:
            WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, work_email_xpath)))
            work_email_field.click()
            time.sleep(3)
            self.assertTrue(work_email_field.is_displayed() and work_email_field.is_enabled(), "'Work email address' field is not clickable")
        except TimeoutException:
            self.fail("'Work email address' field not interactive")

    def test_invalid_email_format_prompt(self):
        work_email_xpath = '//*[@id="contact-new-form"]/div[3]/div[2]/p/span/input'
        another_field_xpath = '//*[@id="contact-new-form"]/div[4]/div[2]/p/span/input'

        def generate_invalid_email():
            characters = string.ascii_letters + string.digits
            random_length = random.randint(1, 20)
            return "".join(random.choice(characters) for _ in range(random_length))

        work_email_field = self.driver.find_element(By.XPATH, work_email_xpath)

        for _ in range(11):
            invalid_email = generate_invalid_email()
            work_email_field.send_keys(invalid_email)
            self.driver.find_element(By.XPATH, another_field_xpath).click()  # Trigger validation
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".email-error-message"))
            )
            error_message = self.driver.find_element(By.CSS_SELECTOR, ".email-error-message").text
            self.assertTrue("invalid email format" in error_message.lower(), f"Error message not found for input: {invalid_email}")
            work_email_field.clear()

        work_email_field.clear()
        self.driver.find_element(By.XPATH, another_field_xpath).click()  # Ensure form ends in a known state

if __name__ == "__main__":
    unittest.main()
