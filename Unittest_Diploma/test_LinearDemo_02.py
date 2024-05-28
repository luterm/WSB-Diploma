import unittest
import random
import string

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time

class LinearDemo(unittest.TestCase):

    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.fake = Faker()

    def tearDown(self):
        self.driver.quit()

    def test_linear_flow_testing_02(self):
        
        self.driver.get("https://jignect.tech/")
        
# 1. Check the if the web title is as expected
        self.assertTrue("Software and QA Testing Company| JigNect Technologies Pvt Ltd" in self.driver.title, "Expected text not found in page title")
        
# 2. Check if the 'contact us' button is displayed properely
        contact_us_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/nav/ul/li[8]/a")
        self.assertTrue(contact_us_button.is_displayed(), "The 'contact us button' element not displayed")

# 3. Check if the 'contact us' button is clickable and redirects the expected subpage of the expected title
        contact_us_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/nav/ul/li[8]/a").click()
        self.assertTrue("Contact Us | JigNect Technologies Pvt Ltd" in self.driver.title, "Expected text not found in page title")

# 4. Check if the 'contact-new-form' element is displayed properely
        conact_new_form = self.driver.find_element(By. CSS_SELECTOR, "#contact-new-form")
        self.assertTrue(conact_new_form.is_displayed(), "The element 'contact_new_form' not displayed")

# 5. Check if desired text header appears on the 'contact us box'
        contact_us_header = self.driver.find_element(By.CSS_SELECTOR, "div[class='contact-title'] h2").text
        self.assertEqual(contact_us_header, "Let's talk", "Contact Us welcome message not displayed")

# 6. Check if the 'contact us box' displays expected 'contact message' 
        contact_message = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(2) > div > p > span > textarea")
        placeholder = contact_message.get_attribute("placeholder")
        self.assertEqual(placeholder, "Do you have any specific requirements? Please let us know and we can include them in the discussion.", "Expected text not present")


# 7. Check if the 'fields have an error' message is not present before 'submit button' clicked with fields left empty
            
        error_message_element = self.driver.find_element(By.XPATH, "//*[@id='wpcf7-f4408-p4307-o1']/form/div[3]")
        self.assertFalse(error_message_element.is_displayed(), "Unexpected field error message")
        

# 8. Check if the expected validation message is displayed properely when the 'contact new form' fields clicked and left empty and the 'submit' button clicked.

            # Find and click 'contact new form' textarea, leave it empty.
        self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(2) > div > p > span > textarea").click()

            # Find and click 'full name' textbox, leave it empty.
        self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(3) > div:nth-child(1) > p > span > input").click()

            # Find and click 'work email address' textbox on the, leave it empty.
        self.driver.find_element(By.CSS_SELECTOR, "span[id='checkboxOne']").click()

            # Find and click 'company' textbox, leave it empty.
        self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(4) > div:nth-child(1) > p > span > input").click()

            # Find and click 'phone number' textbox, leave it empty.
        self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(4) > div:nth-child(2) > p > span > input").click()

            # Leave the 'I agree to have Jignect contact' checkbox unmarked

            # Find and click 'Submit' button on the 'contact new form'.
        self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(6) > div > p > input").click()
        
            # validation message set as variable
        expected_validation_message = 'The field is required.'

            # 'contact new form' textarea validation message check
        textarea_actual_validation_message = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(2) > div > p > span > span").text
        self.assertEqual(textarea_actual_validation_message, expected_validation_message, "'Textarea' validation message does not match")

            # 'full name' textbox validation message check 
        full_name_actual_validation_message = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(3) > div:nth-child(1) > p > span > span").text
        self.assertEqual(full_name_actual_validation_message, expected_validation_message, "'Full name' validation message does not match")

            # 'work email address' field validation message presence check
        email_actual_validation_message = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(3) > div:nth-child(2) > p > span > span").text
        self.assertEqual(email_actual_validation_message, expected_validation_message, "'Email' validation message does not match")

            # 'company'
        company_actual_validation_message = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(4) > div:nth-child(2) > p > span > span").text
        self.assertEqual(company_actual_validation_message, expected_validation_message, "'Company' validation message does no match")
        
            # 'phone number' field validation message presence check
        phone_number_actual_validation_message = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(4) > div:nth-child(2) > p > span > span").text
        self.assertEqual(phone_number_actual_validation_message, expected_validation_message, "'Phone number' validation message does not match")

            # 'I agree to have Jignect contact' checkbox validation message presence check
        contact_agreement_box = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(5) > div > p > span > span.wpcf7-not-valid-tip").text
        self.assertEqual(contact_agreement_box, expected_validation_message, "'Contact agreement' validation message does not match")


# 9. Check if 'One or more fields have an error' message is present; has appeared. 
        fields_have_an_error_message = self.driver.find_element(By.XPATH, "//*[@id='wpcf7-f4408-p4307-o1']/form/div[3]")
        self.assertTrue(fields_have_an_error_message.is_displayed(), "'fields have an error message' field did not appeared'")


# 10. Check if the 'contact new form' saves 'user message' properely to the proper value.

            # a random 'user message' assigned to the variable, text generated and sent to the textbox and checked if saved in a dedicated value properely
        characters = string.ascii_letters + string.digits + string.punctuation
        user_message = "".join(random.choice(characters) for _ in range(1222))
        self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(2) > div > p > span > textarea").send_keys(characters)

            # checking if the 'user message' has been saved succesfully
        user_message_value = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(2) > div > p > span > textarea")
        value = user_message_value.get_attribute("value")
        self.assertEqual(value, characters, "Expected user input not present")


# 11. Check if the 'Full name field' saves input correctly to the value of web placeholder.  

        full_name = self.fake.name()
        full_name_field = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(3) > div:nth-child(1) > p > span > input").send_keys(full_name)
        full_name_value = self.driver.find_element(By.CSS_SELECTOR, "#contact-new-form > div:nth-child(3) > div:nth-child(1) > p > span > input").get_attribute("value")
        self.assertEqual(full_name, full_name_value, "'Full name' value missing")

# 12. Check if the 'user message' textarea 'validation message' disappears after moving to the next required field - being clicked and left empty:

        textarea_actual_validation_message_locator = (By.CSS_SELECTOR, "#contact-new-form > div:nth-child(2) > div > p > span > span")
        try:
            WebDriverWait(self.driver, 1).until(EC.invisibility_of_element_located(textarea_actual_validation_message_locator))
            textarea_actual_validation_message_disappeared = True
        except TimeoutException:
            textarea_actual_validation_message_disappeared = False
        self.assertTrue(textarea_actual_validation_message_disappeared, "'Textarea' validation message still appears")

# 13 Check if the 'Full name' textarea 'validation message' disappears after moving to the next required field - being clicked and left empty:

        company = self.driver.find_element(By.XPATH, '//*[@id="contact-new-form"]/div[4]/div[1]/p/span/input').click()
        full_name_actual_validation_message_locator = (By.XPATH, '//*[@id="contact-new-form"]/div[3]/div[1]/p/span/span')
        try:
            WebDriverWait(self.driver, 1).until(EC.invisibility_of_element_located(full_name_actual_validation_message_locator))
            full_name_actual_validation_message_disappeared = True
        except TimeoutException:
            full_name_actual_validation_message_disappeared = False
            self.assertTrue(full_name_actual_validation_message_disappeared, "'Full name' validation message still appears")

# 14 Check if the 'Company' is interactive and saves 'user text' properely to the value:
        # disscuss with ChatGPT how deep this test can reach and what properties of this element we can check before passing user's input!!!!
        
        company_name = "".join(random.choice(characters) for _ in range(12))
        self.driver.find_element(By.XPATH, '//*[@id="contact-new-form"]/div[4]/div[1]/p/span/input').send_keys(characters)
        time.sleep(3)
        company_name_value = self.driver.find_element(By.CSS_SELECTOR, '#contact-new-form > div:nth-child(4) > div:nth-child(1) > p > span > input')
        value = company_name_value.get_attribute("value")
        self.assertEqual(value, characters, "Expected user input not present")
        # TC014 to be checked, not working as expected. 

# 15. Check if the 'Work email address' is clicable and saves 'user message' properely to the value

        work_email_address_field = (By.XPATH, '//*[@id="contact-new-form"]/div[3]/div[2]/p/span/input')

        try:
            work_email_address_field_is_clickable = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(work_email_address_field))
            work_email_address_field = True
            work_email_address_field_is_clickable.click()
            time.sleep(3)
        except TimeoutException:
            work_email_address_field = False
            self.assertTrue(work_email_address_field, "'Work email address' field not interactive")

# 16. Check if the 'Work email address' returns an invalid email format prompt correctly in case of a random, non-email format input.





        # 15. Check if the 'Phoone number' is clicable and saves 'user message' properely to the value
        # 16. Check if the validation message disappears if all of the 'contact new form' required fields are fulfilled but 'I agree...' checkbox left unmarked.

    
# It is mandatory when you want to run code using command prompt
if __name__ == '__main__':
    unittest.main()

#fill up fields, one by one to check if the validation message dissappears - in progress

#check if the 'agree...' box left unmarked allows to pass the submission in case of input data as email and phone are in correct format
#check that in case of incorrect email/phone number format aproppriate message is displayed - use generator?
# Create a testCase to check if there is a limit of digits in the box for mail and phone number as well (two test cases)