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

        
    def test_linear_flow_testing_v1(self):
        # Navigate to desired web page and verify web page is displayed
        self.driver.get("https://jignect.tech/")
        #self.assertTrue("Softwqwware and QA Testing Company| JigNect Technologies Pvt Ltd" in self.driver.title) 
        self.assertTrue("Software and QA Testing Company| JigNect Technologies Pvt Ltd" in self.driver.title, "Expected text not found in page title")


# Create a separated testCase checking if the page title is as expected - in original version if it is not, programm is breaking at this point and the web browser is terminated
        

        # Clicka on the contact us button
        contact_us_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/nav/ul/li[8]/a").click() 
# changed incorrect XPATH to actual
       

        # Verify desired page i displayed
        contact_us_header = self.driver.find_element(By.CSS_SELECTOR, "div[class='contact-title'] h2").text
        
        self.assertEqual(contact_us_header, "Let's talk", "Contact Us page does not displayed")

        # Generate random string
        full_name = "".join(random.choice(string.ascii_letters) for _ in range(11))

        # Enter value in full name and company name, select checkbox and click on submit button
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Full name']").send_keys(full_name)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Company']").send_keys("Bulepa")
        time.sleep(3)
        

# Create a testcase to check if the web accepts incorrect mail formats - implement random mail generator? 

# Create a testCase to check if there is a limit of digits in the box for mail and phone number as well (two test cases)

# Create a testcase to check if the phone number can be accepted if includes incorrect syntax or elements (letters, etc) - random phone numbers generator? 

# Create a test case to check if the error message is as expected in case of invalid phone or mail data given


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




    def tearDown(self):
        """Tear down methond to close the browser."""
        self.driver.quit()


# It is mandatory when you want to run code using command prompt
if __name__ == '__main__':
    unittest.main()