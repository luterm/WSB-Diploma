import unittest
import random
import string
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

class LinearDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.fake = Faker()

    def tearDown(self):
        self.driver.quit()

    def wait_for_element(self, by, value, timeout=5):
        """Wait for an element to be present on the page."""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))
        except TimeoutException:
            self.fail(f"Element not found: {by}={value}")

    def test_linear_flow_testing_05(self):
        self.driver.get("https://jignect.tech/")

        # Define the locators
        contact_us_button_locator = (By.XPATH, "//nav/ul/li[8]/a")
        contact_new_form_locator = (By.CSS_SELECTOR, "#contact-new-form")
        contact_us_header_locator = (By.CSS_SELECTOR, "div.contact-title h2")
        contact_message_locator = (By.CSS_SELECTOR, "#contact-new-form textarea[placeholder]")
        error_message_element_locator = (By.XPATH, "//*[@id='wpcf7-f4408-p4307-o1']/form/div[3]")
        fields_have_an_error_message_locator = (By.XPATH, "//*[@id='wpcf7-f4408-p4307-o1']/form/div[3]")
        textarea_locator = (By.CSS_SELECTOR, "#contact-new-form > div:nth-child(2) > div > p > span > span")
        full_name_locator = (By.CSS_SELECTOR, "#contact-new-form > div:nth-child(3) > div:nth-child(1) > p > span > input")
        full_name_validation_locator = (By.XPATH, '//*[@id="contact-new-form"]/div[3]/div[1]/p/span/span')
        company_name_locator = (By.XPATH, '//*[@id="contact-new-form"]/div[4]/div[1]/p/span/input')
        work_email_address_locator = (By.XPATH, '//*[@id="contact-new-form"]/div[3]/div[2]/p/span/input')
        invalid_email_format_locator = (By.XPATH, '//*[@id="contact-new-form"]/div[3]/div[2]/p/span/span')


# TC_01. Check if the web title is as expected
        self.assertIn("Software and QA Testing Company| JigNect Technologies Pvt Ltd", self.driver.title, 
              "Expected text not found in page title")

# TC_02. Check if the 'contact us' button is displayed properly
        contact_us_button = self.wait_for_element(*contact_us_button_locator)
        self.assertTrue(contact_us_button.is_displayed(), "The 'contact us button' element not displayed")

# TC_03. Check if the 'contact us' button is clickable and redirects to the expected subpage
        contact_us_button.click()
        self.assertEqual(self.driver.current_url, "https://jignect.tech/contact-us/", "Incorrect page after clicking 'contact us' button")

# TC_04. Check if the 'contact us' page has the correct header
        contact_us_header = self.wait_for_element(*contact_us_header_locator)
        self.assertEqual(contact_us_header.text, "Contact Us", "Incorrect header on 'contact us' page")

# TC_05. Check if the contact form is displayed
        contact_form = self.wait_for_element(*contact_new_form_locator)
        self.assertTrue(contact_form.is_displayed(), "Contact form not displayed")

# TC_06. Check if the contact form has all the necessary fields
        full_name_field = self.wait_for_element(*full_name_locator)
        self.assertTrue(full_name_field.is_displayed(), "Full name field not displayed")

        email_field = self.wait_for_element(*work_email_address_locator)
        self.assertTrue(email_field.is_displayed(), "Email field not displayed")

        message_field = self.wait_for_element(*textarea_locator)
        self.assertTrue(message_field.is_displayed(), "Message field not displayed")

# TC_07. Check if the contact form can be submitted with valid data
        full_name_field.send_keys(self.fake.name())
        email_field.send_keys(self.fake.email())
        message_field.send_keys(self.fake.text())
        contact_form.submit()

        # Wait for the success message to appear and check its text
        success_message = self.wait_for_element(By.CSS_SELECTOR, "#wpcf7-f4408-p4307-o1 > form > div.wpcf7-response-output")
        self.assertEqual(success_message.text, "Thank you for your message. It has been sent.", "Incorrect success message after form submission")

# TC_08. Check if the contact form shows an error when submitted with invalid data
        full_name_field.clear()
        email_field.clear()
        message_field.clear()

        full_name_field.send_keys(self.fake.name())
        email_field.send_keys("invalid email")
        message_field.send_keys(self.fake.text())
        contact_form.submit()

    # Wait for the error message to appear and check its text
        error_message = self.wait_for_element(*invalid_email_format_locator)
        self.assertEqual(error_message.text, "The e-mail address entered is invalid.", "Incorrect error message for invalid email")

# TC_09. Check if the contact form shows an error when submitted with empty fields
        full_name_field.clear()
        email_field.clear()
        message_field.clear()
        contact_form.submit()

    # Wait for the error message to appear and check its text
        error_message = self.wait_for_element(*fields_have_an_error_message_locator)
        self.assertEqual(error_message.text, "One or more fields have an error. Please check and try again.", "Incorrect error message for empty fields")

# TC_10. Check if the contact form shows an error when submitted with only spaces in fields
        full_name_field.send_keys("   ")
        email_field.send_keys("   ")
        message_field.send_keys("   ")
        contact_form.submit()

    # Wait for the error message to appear and check its text
        error_message = self.wait_for_element(*fields_have_an_error_message_locator)
        self.assertEqual(error_message.text, "One or more fields have an error. Please check and try again.", "Incorrect error message for fields with only spaces")

# TC_11. Check if the contact form shows an error when submitted with too long data
        full_name_field.clear()
        email_field.clear()
        message_field.clear()

        full_name_field.send_keys("a" * 256)
        email_field.send_keys(self.fake.email())
        message_field.send_keys(self.fake.text())
        contact_form.submit()

    # Wait for the error message to appear and check its text
        error_message = self.wait_for_element(*full_name_error_locator)
        self.assertEqual(error_message.text, "The full name field is too long.", "Incorrect error message for too long full name")

# TC_12. Check if the contact form shows an error when submitted with too short data
        full_name_field.clear()
        email_field.clear()
        message_field.clear()

        full_name_field.send_keys("a")
        email_field.send_keys(self.fake.email())
        message_field.send_keys(self.fake.text())
        contact_form.submit()

    # Wait for the error message to appear and check its text
        error_message = self.wait_for_element(*full_name_error_locator)
        self.assertEqual(error_message.text, "The full name field is too short.", "Incorrect error message for too short full name")

# TC_13. Check if the contact form shows an error when submitted with special characters in the name field
        full_name_field.clear()
        email_field.clear()
        message_field.clear()

        full_name_field.send_keys("@#$%^&*()")
        email_field.send_keys(self.fake.email())
        message_field.send_keys(self.fake.text())
        contact_form.submit()

        # Wait for the error message to appear and check its text
        error_message = self.wait_for_element(*full_name_error_locator)
        self.assertEqual(error_message.text, "The full name field should only contain letters.", "Incorrect error message for special characters in full name")

# TC_14. Check if the contact form shows an error when submitted with numbers in the name field
        full_name_field.clear()
        email_field.clear()
        message_field.clear()

        full_name_field.send_keys("1234567890")
        email_field.send_keys(self.fake.email())
        message_field.send_keys(self.fake.text())
        contact_form.submit()

        # Wait for the error message to appear and check its text
        error_message = self.wait_for_element(*full_name_error_locator)
        self.assertEqual(error_message.text, "The full name field should only contain letters.", "Incorrect error message for numbers in full name")