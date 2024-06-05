import unittest
import random
import string
import logging
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

# Set up logging:
logging.basicConfig(filename='test_log.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Set up the test case class:
class LinearDemo(unittest.TestCase):

    def setUp(self):
        logging.info('Setting up the test')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.fake = Faker()

    def tearDown(self):
        logging.info('Tearing down the test')
        self.driver.quit()

    def wait_for_element(self, by, value, timeout=5):
        # Wait for an element to be present on the page:
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))
        except TimeoutException:
            self.fail(f"Element not found: {by}={value}")

    def test_linear_flow_testing_04(self):
        logging.info('Starting test_linear_flow_testing_04')
        self.driver.get("https://jignect.tech/")

        # Define the locators:
        company_name_field = (By.XPATH, '//*[@id="contact-new-form"]/div[4]/div[1]/p/span/input')
        contact_us_button = (By.XPATH, "//nav/ul/li[8]/a")
        contact_new_form = (By.CSS_SELECTOR, "#contact-new-form")
        contact_us_header = (By.CSS_SELECTOR, "div.contact-title h2")
        contact_us_invitation_placeholder = (By.CSS_SELECTOR, "#contact-new-form textarea[placeholder]")
        full_name_field = (By.CSS_SELECTOR, "#contact-new-form > div:nth-child(3) > div:nth-child(1) > p > span > input")
        full_name_validation_message = (By.CSS_SELECTOR, "#contact-new-form > div:nth-child(3) > div:nth-child(1) > p > span > span")
        contact_us_textarea = (By.CSS_SELECTOR, '#contact-new-form > div:nth-child(2) > div > p > span > textarea')
        invalid_email_format_prompt = (By.XPATH, '//*[@id="contact-new-form"]/div[3]/div[2]/p/span/span')
        phone_field = (By.XPATH, '//*[@id="contact-new-form"]/div[4]/div[2]/p/span/input')
        submit_button = (By.CSS_SELECTOR, "#contact-new-form > div:nth-child(6) > div > p > input")
        text_area_validation_message = (By.CSS_SELECTOR, "#contact-new-form > div:nth-child(2) > div > p > span > span")
        work_email_address_field = (By.XPATH, '//*[@id="contact-new-form"]/div[3]/div[2]/p/span/input')
    

# TC_01. Check if the web title is as expected
        self.assertIn("Software and QA Testing Company| JigNect Technologies Pvt Ltd", self.driver.title, 
                      "Expected text not found in page title")

# TC_02. Check if the 'contact us' button is displayed properly
        contact_us_button = self.wait_for_element(*contact_us_button)
        self.assertTrue(contact_us_button.is_displayed(), "The 'contact us button' element not displayed")

# TC_03. Check if the 'contact us' button is clickable and redirects to the expected subpage
        contact_us_button.click()
        WebDriverWait(self.driver, 5).until(EC.title_contains("Contact Us | JigNect Technologies Pvt Ltd"))
        self.assertIn("Contact Us | JigNect Technologies Pvt Ltd", self.driver.title, 
                      "Expected text not found in page title after clicking 'Contact Us'")

# TC_04. Check if the 'contact-new-form' element is displayed properly
        contact_new_form = self.wait_for_element(*contact_new_form)
        self.assertTrue(contact_new_form.is_displayed(), "The element 'contact_new_form' not displayed")

# TC_05. Check if the 'contact us' box displays the expected text header
        welcome_text = self.driver.find_element(*contact_us_header).text
        self.assertEqual(welcome_text, "Let's talk", "Contact Us welcome message not displayed")

# TC_06. Check if the 'contact us box' displays the expected 'default contact message' 
        default_contact_message = self.driver.find_element(*contact_us_invitation_placeholder)
        placeholder_default_text = default_contact_message.get_attribute("placeholder")
        self.assertEqual(placeholder_default_text, 
                 "Do you have any specific requirements? Please let us know and we can include them in the discussion.",
                 "Expected text not present")
        value_before_typing = default_contact_message.get_attribute("value")
        self.assertEqual(value_before_typing, "", "Textarea is not empty before typing") 

# TC_07. Check if the 'contact us textarea' default text disappears after clicking and typing
        textarea = self.driver.find_element(*contact_us_textarea)
        textarea.send_keys("Bulepa")
        value_after_typing = textarea.get_attribute("value")
        self.assertNotEqual(value_after_typing, "", "Textarea is empty after typing")

        # Clear the textarea after the test
        textarea.clear()

# TC_08. Check if the 'fields have an error' message is not present before the 'submit button' is clicked
        error_message_element = self.driver.find_element(By.XPATH, "//*[@id='wpcf7-f4408-p4307-o1']/form/div[3]")
        self.assertFalse(error_message_element.is_displayed(), "Unexpected 'fields have an error' message")

# TC_09. Check validation messages presence after clicking and leaving fields empty, then clicking the 'submit' button
        self.driver.find_element(*contact_us_textarea).click() # contact_us_textarea field
        self.driver.find_element(*full_name_field).click() # full_name_field
        self.driver.find_element(*work_email_address_field).click() # work_email_address_field
        self.driver.find_element(*company_name_field).click() # company_name_field
        self.driver.find_element(*phone_field).click() # phone_field

        # click 'submit button'
        self.driver.find_element(*submit_button).click() 

        expected_validation_message = 'The field is required.'

        # Validate each required field's validation message, crate the list of tuples
        fields = [
            (By.CSS_SELECTOR, "#contact-new-form > div:nth-child(2) > div > p > span > span"),
            (By.CSS_SELECTOR, "#contact-new-form > div:nth-child(3) > div:nth-child(1) > p > span > span"),
            (By.CSS_SELECTOR, "#contact-new-form > div:nth-child(3) > div:nth-child(2) > p > span > span"),
            (By.CSS_SELECTOR, "#contact-new-form > div:nth-child(4) > div:nth-child(1) > p > span > span"),
            (By.CSS_SELECTOR, "#contact-new-form > div:nth-child(4) > div:nth-child(2) > p > span > span"),
            (By.CSS_SELECTOR, "#contact-new-form > div:nth-child(5) > div > p > span > span.wpcf7-not-valid-tip") # 'agree to contact' checkbox validation field
        ]

        for validation_message_locator in fields:
            validation_message = self.driver.find_element(*validation_message_locator).text
            self.assertEqual(validation_message, expected_validation_message, 
                             f"Validation message mismatch: {validation_message}")

# TC_10. Check if 'One or more fields have an error' message is present
        fields_have_an_error_message = self.driver.find_element(By.XPATH, "//*[@id='wpcf7-f4408-p4307-o1']/form/div[3]")
        self.assertTrue(fields_have_an_error_message.is_displayed(), "'Fields have an error message' did not appear")

# TC_11. Check if the 'contact new form' textarea is clickable and clears the text put by user
        
        # Verify that the textarea is clickable
        self.assertTrue(self.driver.find_element(*contact_us_textarea).is_enabled(), "The 'contact new form' textarea is not clickable")

        # Enter some text in the textarea
        user_message = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(1222))
        self.driver.find_element(*contact_us_textarea).send_keys(user_message)

        # Verify that the entered text is present in the textarea
        textarea_value = self.driver.find_element(*contact_us_textarea).get_attribute("value")
        self.assertEqual(textarea_value, user_message, "The entered text is not present in the textarea")

        # Clear the textarea
        self.driver.find_element(*contact_us_textarea).clear()

        # Verify that the textarea is empty
        textarea_value = self.driver.find_element(*contact_us_textarea).get_attribute("value")
        self.assertEqual(textarea_value, "", "The textarea was not cleared")

# TC_12. Check if the 'contact new form' textarea 'validation message' disappears after being fulfilled and FULL_NAME_FIELD clicked
       
        # Identify the text input field and send the example user text
        text_input_field = self.driver.find_element(*contact_us_textarea)#contact-new-form > div:nth-child(2) > div > p > span > span
        text_input_field.send_keys('example user text about Bulepa')
       
        # Click the 'Full name' field
        full_name_field_element = self.driver.find_element(*full_name_field)
        full_name_field_element.click()

        try:
            WebDriverWait(self.driver, 2).until(EC.invisibility_of_element_located(text_area_validation_message))
        except TimeoutException:
            self.fail("'Textarea' validation message still appears")

        WebDriverWait(self.driver, 1) # CHECK THE LOGIC between TC_10 and TC_11

# TC_13. Check if the 'Full name' validation message is still present if the field being clicked and left empty
        full_name_field_element = self.driver.find_element(*full_name_field)
        full_name_field_element.click()

        # Click somewhere else on the page to trigger the validation
        self.driver.find_element(By.TAG_NAME, 'body').click()

        try:
            WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(full_name_validation_message))
        except TimeoutException:
            self.fail("'Full name' validation message does not appear")

# TC_14. Check if the 'Full name' field saves input correctly
        full_name = self.fake.name()
        full_name_field_element = self.wait_for_element(*full_name_field)
        full_name_field_element.send_keys(full_name)
        full_name_value = self.driver.find_element(*full_name_field).get_attribute("value")
        self.assertEqual(full_name, full_name_value, "'Full name' value missing")

# TC_15. Check if the 'Company' field is interactive and saves 'user input' properly
        company_name = "".join(random.choice(string.ascii_letters) for _ in range(12))
        self.driver.find_element(*company_name_field).send_keys(company_name)
        company_name_value = self.driver.find_element(*company_name_field).get_attribute("value")
        self.assertEqual(company_name_value, company_name, "Expected user input not present in 'Company' field")

# TC_16. Check if the 'Work email address' is clickable and saves 'user message' properly
        fake_email = self.fake.email()
        try:                                       
            work_email_address_is_clickable = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(work_email_address_field))
            work_email_address_input = self.driver.find_element(*work_email_address_field)
            work_email_address_input.send_keys(fake_email)
            saved_email = work_email_address_input.get_attribute("value")
            self.assertEqual(fake_email, saved_email, "Work email address field did not save the input correctly")
        except TimeoutException:
            self.fail("Work email address field not clickable")

        # Clear the field after the test
        work_email_address_input.clear()

# TC_17. Check if the invalid email validation message appears properly
        
        def generate_invalid_email():

            # Create different types of invalid emails:
            types_of_invalid_emails = [
                lambda: "".join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 10))),  # No '@' symbol
                lambda: "".join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 10))) + "@",  # No domain after @
                lambda: "@" + "".join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 10))),  # Starts with @
                lambda: "".join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 10))) + "@example",  # No top-level domain
                lambda: "".join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 10))) + "@example.",  # No domain after dot
                lambda: "".join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 10))) + "@example.123"  # Numeric top-level domain
            ]
            return random.choice(types_of_invalid_emails)()
            
        work_email_input = self.driver.find_element(*work_email_address_field)
        phone_field = self.driver.find_element(By.XPATH, '//*[@id="contact-new-form"]/div[4]/div[2]/p/span/input')

        for _ in range(11):
            invalid_email = generate_invalid_email()
            work_email_input.send_keys(invalid_email)
            phone_field.click()

            try:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(invalid_email_format_prompt))
                error_message = self.driver.find_element(*invalid_email_format_prompt).text
                self.assertIn("invalid email format", error_message.lower(), f"Email format error message not found for input: {invalid_email}")
            except TimeoutException:
                self.fail(f"Email format error message did not appear for input: {invalid_email}")

            work_email_address_field.clear()

if __name__ == "__main__":
    unittest.main()

    # CHECK THE LOGIC ORDER OF THE TEST CASES ONCE AGAIN
    # CONSIDER ADDITIONAL TEST CASES    
    # CHECK IN THE PREVIOUS VERSION OF THE CODE: NoSuchElementException place and usage
